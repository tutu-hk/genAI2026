#!/usr/bin/env node
/**
 * Calls Poe API (Nano-Banana-Pro or fallback text model) to analyze poster.html
 * and write suggestions / improved content to betterPoster.md.
 * API key is read from AmbassadorProgramme/LLM/poeKey.md (first line).
 */

const fs = require('fs');
const path = require('path');
const OpenAI = require('openai').default;

const DIR = path.join(__dirname, '..');
const KEY_FILE = path.join(DIR, '..', 'LLM', 'poeKey.md');
const POSTER_HTML = path.join(DIR, 'posters', 'poster.html');
const OUT_FILE = path.join(DIR, 'docs', 'betterPoster.md');

const POE_BASE = 'https://api.poe.com/v1';
const MODEL = process.env.POE_POSTER_MODEL || 'Nano-Banana-Pro';

function getKey() {
  if (!fs.existsSync(KEY_FILE)) {
    console.error('Missing API key file:', KEY_FILE);
    console.error('See AmbassadorProgramme/LLM/dummyPoe.md for setup.');
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

  const systemPrompt = `You are a design and copy expert for event posters. Output only valid markdown. No preamble or "here is" text—start directly with the markdown content.`;

  const userPrompt = `Analyze this HTML for a workshop poster. Produce a single markdown document that includes:

1. **Summary** – In 2–3 sentences, what the poster conveys (event, audience, CTA).
2. **Suggestions** – Concrete improvements for design, layout, copy, or clarity (bulleted list).
3. **Optional revised copy** – If you suggest different wording for the title, tagline, or CTA, provide it in a short section.

Output only the markdown document, no code fences or explanation before/after.

HTML:
\`\`\`html
${html}
\`\`\``;

  console.log('Calling Poe API, model:', MODEL);
  let completion;
  try {
    completion = await client.chat.completions.create({
      model: MODEL,
      messages: [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: userPrompt },
      ],
      stream: false,
    });
  } catch (err) {
    if (err.status === 404 || (err.message && err.message.includes('model'))) {
      console.error('Model "%s" may not be available on Poe. Try POE_POSTER_MODEL=Claude-Sonnet-4 npm run better', MODEL);
    }
    throw err;
  }

  const text = completion.choices[0]?.message?.content?.trim();
  if (!text) {
    console.error('Empty response from API');
    process.exit(1);
  }

  fs.writeFileSync(OUT_FILE, text, 'utf8');
  console.log('Written:', OUT_FILE);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
