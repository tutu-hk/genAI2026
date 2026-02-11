#!/usr/bin/env python3
"""
OCR script for handwritten notes with strikeout detection.
Uses HKBU GenAI API (Azure OpenAI) to process handwritten text and skip striked-out content.
"""

import os
import sys
import base64
import subprocess
import json
import urllib.request
from datetime import datetime
from pathlib import Path

def log_progress(log_file, message):
    """Log progress and flush immediately for real-time updates."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_msg = f"{timestamp} - {message}"
    print(log_msg)
    with open(log_file, 'a') as f:
        f.write(log_msg + "\n")
        f.flush()

def encode_image_base64(image_path):
    """Encode image to base64 for API calls."""
    with open(image_path, "rb") as image_file:
        return base64.standard_b64encode(image_file.read()).decode("utf-8")

def get_api_key():
    """Prompt user for HKBU GenAI API key."""
    print("\n" + "=" * 60)
    print("HKBU GenAI API Key Required")
    print("Get your key from: https://genai.hkbu.edu.hk/settings/api-docs")
    print("=" * 60)
    api_key = input("Enter your HKBU GenAI API key: ").strip()
    if not api_key:
        print("ERROR: API key cannot be empty")
        sys.exit(1)
    return api_key

def get_model_name():
    """Prompt user for model name (optional)."""
    print("\n" + "-" * 60)
    print("Model Selection (check https://genai.hkbu.edu.hk/settings/api-docs)")
    print("Press Enter to auto-detect, or type a specific model name:")
    print("-" * 60)
    model = input("Model name (or Enter to auto-detect): ").strip()
    return model if model else None

def ocr_with_hkbu_api(image_path, api_key, log_file):
    """Use HKBU GenAI API (Azure OpenAI) for OCR with strikeout detection."""
    
    log_progress(log_file, "Encoding image for HKBU GenAI API...")
    base64_image = encode_image_base64(image_path)
    
    # Determine image type from extension
    ext = Path(image_path).suffix.lower()
    mime_type = "image/jpeg" if ext in [".jpg", ".jpeg"] else "image/png"
    
    log_progress(log_file, "Preparing request to HKBU GenAI API...")
    
    # HKBU GenAI Platform available models (with vision capability)
    # API Version: 2024-12-01-preview
    # gpt-5 is the most capable for OCR tasks
    models_to_try = [
        "gpt-5",
        "o1",
        "gpt-4.1",
        "gpt-5-mini",
        "gpt-4.1-mini",
        "o3-mini"
    ]
    
    api_version = "2024-12-01-preview"
    
    system_prompt = """You are an OCR expert specializing in handwritten text recognition.
Your task is to:
1. Carefully read and transcribe all handwritten text from the image
2. SKIP any text that is crossed out/striked through - do not include it in your output
3. Preserve the original structure and formatting as much as possible
4. Use markdown formatting for the output
5. If text is unclear, make your best interpretation but indicate uncertainty with [?]
6. Maintain paragraph breaks and list structures from the original

Only output the transcribed text, no explanations."""

    base_payload = {
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Please transcribe the handwritten text from this image. Skip any text that is crossed out or striked through."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:{mime_type};base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 4096
    }
    
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }
    
    last_error = None
    for model in models_to_try:
        url = f"https://genai.hkbu.edu.hk/general/rest/deployments/{model}/chat/completions?api-version={api_version}"
        log_progress(log_file, f"Trying model: {model}...")
        
        # Build payload - some models don't support temperature
        payload = base_payload.copy()
        if model not in ["o1", "o3-mini", "gpt-5", "gpt-5-mini"]:
            payload["temperature"] = 0.1
        
        try:
            data = json.dumps(payload).encode('utf-8')
            req = urllib.request.Request(url, data=data, headers=headers, method='POST')
            
            with urllib.request.urlopen(req, timeout=120) as response:
                result = json.loads(response.read().decode('utf-8'))
                
            log_progress(log_file, f"Success with model: {model}")
            
            if 'choices' in result and len(result['choices']) > 0:
                return result['choices'][0]['message']['content']
            else:
                raise Exception(f"Unexpected API response format: {result}")
                
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8') if e.fp else str(e)
            log_progress(log_file, f"Model {model} failed ({e.code}): {error_body[:100]}...")
            last_error = f"{model}: {e.code} - {error_body}"
            continue
        except Exception as e:
            log_progress(log_file, f"Model {model} error: {str(e)[:100]}...")
            last_error = str(e)
            continue
    
    raise Exception(f"All models failed. Last error: {last_error}")

def ocr_with_tesseract(image_path, log_file):
    """Fallback: Use Tesseract OCR with PIL only (no opencv)."""
    try:
        import pytesseract
        from PIL import Image
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "pytesseract", "pillow", "-q"], check=True)
        import pytesseract
        from PIL import Image
    
    log_progress(log_file, "Using Tesseract OCR as fallback...")
    log_progress(log_file, "Loading image with PIL...")
    
    image = Image.open(image_path)
    # Convert to grayscale
    image = image.convert('L')
    
    log_progress(log_file, "Running Tesseract OCR...")
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image, config=custom_config)
    
    log_progress(log_file, "Tesseract OCR completed")
    log_progress(log_file, "Note: Strikeout detection not available with Tesseract fallback")
    return text

def process_image(image_path, output_file="typed01.md"):
    """Main function to process handwritten image."""
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    log_file = "process.log"
    # Clear previous log
    open(log_file, 'w').close()
    
    log_progress(log_file, "=" * 50)
    log_progress(log_file, "Starting OCR Processing")
    log_progress(log_file, f"Input: {image_path}")
    log_progress(log_file, f"Output: {output_file}")
    log_progress(log_file, "=" * 50)
    
    # Verify input file exists
    if not Path(image_path).exists():
        log_progress(log_file, f"ERROR: Input file not found: {image_path}")
        sys.exit(1)
    
    log_progress(log_file, f"Input file verified: {Path(image_path).stat().st_size} bytes")
    
    # Get HKBU API key from user
    api_key = get_api_key()
    
    # Try HKBU GenAI API first (best for handwritten with strikeout detection)
    text = None
    try:
        log_progress(log_file, "Attempting AI-powered OCR with HKBU GenAI API...")
        text = ocr_with_hkbu_api(image_path, api_key, log_file)
        log_progress(log_file, "AI-powered OCR successful!")
    except Exception as e:
        log_progress(log_file, f"HKBU GenAI API failed: {str(e)}")
        log_progress(log_file, "Falling back to Tesseract OCR...")
        try:
            text = ocr_with_tesseract(image_path, log_file)
        except Exception as e2:
            log_progress(log_file, f"Tesseract also failed: {str(e2)}")
            log_progress(log_file, "ERROR: All OCR methods failed")
            sys.exit(1)
    
    # Write output
    log_progress(log_file, f"Writing output to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# Transcribed Handwritten Notes\n\n")
        f.write(f"*Source: {image_path}*  \n")
        f.write(f"*Processed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
        f.write("---\n\n")
        f.write(text)
    
    log_progress(log_file, "=" * 50)
    log_progress(log_file, "OCR Processing Complete!")
    log_progress(log_file, f"Output written to: {output_file}")
    log_progress(log_file, "=" * 50)
    
    return text

if __name__ == "__main__":
    # Default to the test image
    image_path = "testHandwritten01.jpg"
    
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    
    process_image(image_path)
