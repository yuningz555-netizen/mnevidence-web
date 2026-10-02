"""Production entry point; scientific runtime and frozen models are unchanged."""
import os
import sys
from pathlib import Path

for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(name, "1")

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "backend"))

from threadpoolctl import threadpool_limits
from waitress import serve
from app import app
from model_runtime import models


def main():
    port = int(os.environ.get("PORT", "8781"))
    if not 1 <= port <= 65535:
        raise ValueError("PORT must be between 1 and 65535.")
    models()
    with threadpool_limits(limits=1):
        serve(app, host=os.environ.get("HOST", "0.0.0.0"), port=port,
              threads=4, connection_limit=32, channel_timeout=120,
              max_request_body_size=64 * 1024, ident="MnEvidence")


if __name__ == "__main__":
    main()
