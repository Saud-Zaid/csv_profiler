from __future__ import annotations

from csv import DictReader
from pathlib import Path

import typer

def read_csv_rows(path: str | Path) -> list[dict[str, str]]:

    path = Path(path)
    csv_list: list[dict[str, str]] = []

    if not path.exists():
        raise FileNotFoundError(f"Input file does not exist: {path}")

    with open(path, newline="", encoding="utf-8") as f:
        reader = DictReader(f)

        for row in reader:
            csv_list.append(row)

    if not csv_list:
        raise ValueError("CSV has no data rows")

    return csv_list
