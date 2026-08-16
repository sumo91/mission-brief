import { existsSync } from "node:fs";
import { resolve } from "node:path";
import { pathToFileURL } from "node:url";

const outputPath = resolve("dist/index.html");

if (!existsSync(outputPath)) {
  console.error("Preview output is missing: dist/index.html");
  process.exitCode = 1;
} else {
  console.log(`Preview ready: ${pathToFileURL(outputPath).href}`);
}
