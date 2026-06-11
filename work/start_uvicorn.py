from pathlib import Path
import sys

import uvicorn


ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / "work" / "uvicorn.wrapper.log"
sys.path.insert(0, str(ROOT))


def main() -> None:
    try:
        uvicorn.run(
            "src.main:app",
            host="127.0.0.1",
            port=8000,
            log_level="info",
        )
    except Exception as exc:
        LOG.write_text(f"{type(exc).__name__}: {exc}\n", encoding="utf-8")
        raise


if __name__ == "__main__":
    main()
