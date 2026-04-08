from pathlib import Path

LWCC_HOME = Path.home() / ".lwcc"
WEIGHTS = "weights"

def weights_dir():
    return LWCC_HOME / WEIGHTS
