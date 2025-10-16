import hashlib
import json
import os

# === CONFIGURATION (edit once) ===
GITHUB_USER = "snkdarian"
GITHUB_REPO = "FarmBot"

EXE_PATH = os.path.join("output", "FarmBot.exe")
MANIFEST_PATH = "manifest.json"

# ================================

def sha256_of_file(path, chunk_size=8192):
    """Compute the SHA256 checksum of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()

def main():
    if not os.path.exists(EXE_PATH):
        print(f"[Error] File not found: {EXE_PATH}")
        return

    version = input("Enter version (e.g. 1.2.0): ").strip()
    if not version:
        print("[Error] Version cannot be empty.")
        return

    print("[*] Calculating SHA256...")
    sha = sha256_of_file(EXE_PATH)
    print(f"[OK] SHA256: {sha}")

    # Build URL automatically
    url = f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/releases/download/v{version}/FarmBot.exe"

    manifest = {
        "version": version,
        "url": url,
        "sha256": sha
    }

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(f"[OK] Manifest written to: {MANIFEST_PATH}")
    print(f"[INFO] URL: {url}")

if __name__ == "__main__":
    main()
