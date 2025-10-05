import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        type=lambda path: Path(path).absolute(),
        help="Path to the data directory",
        required=True,
    )

    p = parser.parse_args()
    print(p.data_dir, type(p.data_dir))


if __name__ == "__main__":
    main()
