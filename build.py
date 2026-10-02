"""Expand the versioned runtime archive and verify its allowlisted contents."""
import hashlib
import json
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent


def main():
    manifest = json.loads((ROOT / "release_manifest.json").read_text(encoding="utf-8"))
    archive = ROOT / "runtime.zip"
    if hashlib.sha256(archive.read_bytes()).hexdigest() != manifest["archive_sha256"]:
        raise RuntimeError("Release archive integrity check failed.")
    expected = {item["path"]: item["sha256"] for item in manifest["runtime_files"]}
    with zipfile.ZipFile(archive) as source:
        if set(source.namelist()) != set(expected):
            raise RuntimeError("Unexpected release archive contents.")
        for name in source.namelist():
            path = PurePosixPath(name)
            valid_location = path.parts[0] in {"backend", "frontend", "tests", "third_party"} or name in {"production.py", "requirements.txt"}
            if path.is_absolute() or ".." in path.parts or not valid_location:
                raise RuntimeError("Invalid archive path.")
            payload = source.read(name)
            if hashlib.sha256(payload).hexdigest() != expected[name]:
                raise RuntimeError(f"File integrity check failed: {name}")
            target = ROOT / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(payload)
    print(f"Verified and extracted {len(expected)} runtime files.")


if __name__ == "__main__":
    main()
