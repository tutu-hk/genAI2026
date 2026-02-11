# Ollama Model Options for Chatbot

## Currently Using

The chatbot is configured to use:

```javascript
let ollamaModel = 'llama3.2:1b';
```

**llama3.2:1b** - Meta's Llama 3.2 (1 billion parameters)
- Size: 1.3 GB
- Speed: Very fast responses
- Quality: Good for simple conversations and basic writing assistance
- Best for: Quick prototyping, learning, lightweight tasks

## Currently Installed

| Model | Size | Status |
|-------|------|--------|
| llama3.2:1b | 1.3 GB | ✅ Installed |

## Other Available Models

You can install additional models with `ollama pull <model-name>`:

### Recommended for Better Quality

| Model | Size | Best For | Install Command |
|-------|------|----------|-----------------|
| **llama3.2:3b** | 2.0 GB | Better reasoning, still fast | `ollama pull llama3.2:3b` |
| **llama3.1:8b** | 4.7 GB | High quality, good balance | `ollama pull llama3.1:8b` |
| **gemma2:2b** | 1.6 GB | Google's efficient small model | `ollama pull gemma2:2b` |
| **gemma2:9b** | 5.4 GB | Excellent quality | `ollama pull gemma2:9b` |
| **phi3:mini** | 2.3 GB | Microsoft's capable small model | `ollama pull phi3:mini` |
| **mistral:7b** | 4.1 GB | Strong all-around performance | `ollama pull mistral:7b` |
| **qwen2.5:7b** | 4.7 GB | Good multilingual support | `ollama pull qwen2.5:7b` |

### Coding-Focused Models

| Model | Size | Best For | Install Command |
|-------|------|----------|-----------------|
| **codellama:7b** | 3.8 GB | Code generation and explanation | `ollama pull codellama:7b` |
| **deepseek-coder:6.7b** | 3.8 GB | Strong at coding tasks | `ollama pull deepseek-coder:6.7b` |
| **starcoder2:3b** | 1.7 GB | Lightweight coding assistant | `ollama pull starcoder2:3b` |

### Large Models (Need More RAM)

| Model | Size | RAM Needed | Best For |
|-------|------|------------|----------|
| **llama3.1:70b** | 40 GB | 48+ GB | Near-GPT-4 quality |
| **mixtral:8x7b** | 26 GB | 32+ GB | Strong reasoning |
| **command-r** | 20 GB | 24+ GB | Long context, RAG |

## How to Switch Models

### Method 1: Change in chatbot.html

Edit line 540:
```javascript
let ollamaModel = 'llama3.2:3b';  // Change model name here
```

### Method 2: Install and Test Quickly

```bash
# Install a new model
ollama pull llama3.2:3b

# Test it in terminal
ollama run llama3.2:3b "Hello, how are you?"
```

## Quality vs Speed Tradeoffs

```
Speed (Fast) ←────────────────────────────────────→ Quality (Best)

llama3.2:1b  →  llama3.2:3b  →  llama3.1:8b  →  llama3.1:70b
(1.3 GB)        (2.0 GB)        (4.7 GB)         (40 GB)
```

## Our Codespace Limits

GitHub Codespaces typically have:
- **RAM**: 8-16 GB (depending on machine type)
- **Storage**: Limited, models are large

**Recommended for Codespace**: Stay with models under 5 GB
- ✅ llama3.2:1b (current)
- ✅ llama3.2:3b (good upgrade)
- ✅ gemma2:2b
- ⚠️ llama3.1:8b (may work, near limit)
- ❌ Larger models (won't fit)

## Quick Upgrade Guide

Want better essay assistance? Try:

```bash
# Download slightly larger model (still fits in Codespace)
ollama pull llama3.2:3b

# Then update chatbot.html line 540 to:
# let ollamaModel = 'llama3.2:3b';
```

This gives ~40% better writing quality with minimal speed impact.
