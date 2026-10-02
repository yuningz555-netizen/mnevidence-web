"""WSGI adapter for the same frozen runtime; no scientific-rule changes."""
import os
import sys
from pathlib import Path

for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(name, "1")

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "backend"))

from threadpoolctl import threadpool_limits
from model_runtime import models
from app import app as application

thread_limits = threadpool_limits(limits=1)
models()
