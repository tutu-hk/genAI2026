#!/usr/bin/env node
/**
 * 1. Calls Poe to generate improved poster HTML (from poster.html).
 * 2. Writes result to posterBetter.html.
 * 3. Screenshots posterBetter.html to betterPoster.jpg.
 * Uses AmbassadorProgramme/LLM/poeKey.md for API key.
 * Use a text model (e.g. Claude-Sonnet-4) for HTML output; set POE_POSTER_MODEL if needed.
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const OpenAI = require('openai').default;

const DIR = path.join(__dirname, '..');
const KEY_FILE = path.join(DIR, '..', 'LLM', 'poeKey.md');
const POSTER_HTML = path.join(DIR, 'posters', 'poster.html');
const POSTER_BETTER_HTML = path.join(DIR, 'posters', 'posterBetter.html');
const BETTER_JPG = path.join(DIR, 'output', 'betterPoster.jpg');

const POE_BASE = 'https://api.poe.com/v1';
const MODEL = process.env.POE_POSTER_MODEL || 'Nano-Banana-Pro';

function getKey() {
  if (!fs.existsSync(KEY_FILE)) {
    console.error('Missing API key file:', KEY_FILE);
    process.exit(1);
  }
  const raw = fs.readFileSync(KEY_FILE, 'utf8');
  const line = raw.split('\n')[0].trim();
  if (!line) {
    console.error('First line of', KEY_FILE, 'should be your Poe API key.');
    process.exit(1);
  }
  return line;
}

function extractHtml(text) {
  let out = text.trim();
  const fence = out.match(/^```(?:html)?\s*\n?([\s\S]*?)```/);
  if (fence) out = fence[1].trim();
  return out;
}

async function main() {
  if (!fs.existsSync(POSTER_HTML)) {
    console.error('poster.html not found in', DIR);
    process.exit(1);
  }

  const apiKey = getKey();
  const html = fs.readFileSync(POSTER_HTML, 'utf8');

  const client = new OpenAI({
    apiKey,
    baseURL: POE_BASE,
  });

  const systemPrompt = `You are an expert at improving web posters. You output only valid, complete HTML. No explanation, no markdown code fence—output the raw HTML document only. Keep the same overall structure and CSS class names so the layout still works.`;

  const userPrompt = `Improve this workshop poster HTML to be MORE VISUAL and eye-catching. Return the complete, improved HTML document.

Requirements:
- Make it more visual: add icons (e.g. calendar/clock for date-time, small visual accents), a clear visual badge or pill for "Earn CCL Credits!", subtle dividers or cards to separate sections, and stronger visual hierarchy (title larger/bolder, clear blocks for speaker vs when vs CTA).
- Use inline SVG or emoji for simple icons (📅 🕐 ✓) if no external assets; or CSS shapes/borders to create visual interest. Add a subtle gradient or accent stripe if it helps.
- Keep: one .poster container; same registration URL (https://forms.office.com/r/tB9HqyGmuH); same speaker photo URL (https://lc.hkbu.edu.hk/main/wp-content/uploads/simon-1.jpg); same date/time (Friday, 20 January 2026, 10:00 am – 12:00 noon). Class names can be extended (e.g. .when with an icon inside).
- Improve copy: engaging title/tagline, shorter audience line, active CCL line. Slightly larger tagline, more gap in speaker row, smaller QR.
- Output ONLY the full HTML document (from <!DOCTYPE> to </html>). No \`\`\` or explanation.`;

  const fullPrompt = userPrompt + '\n\nCurrent HTML:\n' + html;

  console.log('Calling Poe to generate improved poster HTML, model:', MODEL);
  let completion;
  try {
    completion = await client.chat.completions.create({
      model: MODEL,
      messages: [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: fullPrompt },
      ],
      stream: false,
    });
  } catch (err) {
    if (err.status === 404 || (err.message && err.message.includes('model'))) {
      console.error('Model "%s" may not be available. Try POE_POSTER_MODEL=Claude-Sonnet-4', MODEL);
    }
    throw err;
  }

  const rawResponse = completion.choices[0]?.message?.content?.trim();
  if (!rawResponse) {
    console.error('Empty response from API');
    process.exit(1);
  }

  const improvedHtml = extractHtml(rawResponse);
  if (!improvedHtml.includes('<!DOCTYPE') && !improvedHtml.includes('<html')) {
    console.error('Response does not look like HTML. First 200 chars:', improvedHtml.slice(0, 200));
    process.exit(1);
  }

  fs.writeFileSync(POSTER_BETTER_HTML, improvedHtml, 'utf8');
  console.log('Written:', POSTER_BETTER_HTML);

  console.log('Screenshotting to betterPoster.jpg...');
  execSync('node screenshot-better.js', { cwd: path.join(DIR, 'scripts'), stdio: 'inherit' });
  console.log('Done:', BETTER_JPG);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
