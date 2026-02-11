#!/usr/bin/env node
/** Copies replit/config.toml to root .replit for Replit deployment. Run: npm run replit:setup */
import { copyFileSync } from "fs";
import { dirname, join } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = join(__dirname, "..");
copyFileSync(join(__dirname, "config.toml"), join(root, ".replit"));
console.log("Created .replit from replit/config.toml");
