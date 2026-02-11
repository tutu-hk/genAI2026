const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

async function main() {
  const dir = __dirname;
  const htmlPath = path.join(dir, '..', 'posters', 'poster.html');
  const outPath = path.join(dir, '..', 'output', 'poster.jpg');

  if (!fs.existsSync(htmlPath)) {
    console.error('poster.html not found');
    process.exit(1);
  }

  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto('file://' + htmlPath, { waitUntil: 'networkidle0' });
  await page.setViewport({ width: 800, height: 1200 });
  const poster = await page.$('.poster');
  if (poster) {
    await poster.screenshot({ path: outPath, type: 'jpeg', quality: 92 });
  } else {
    await page.screenshot({ path: outPath, type: 'jpeg', quality: 92 });
  }
  await browser.close();
  console.log('Saved:', outPath);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
