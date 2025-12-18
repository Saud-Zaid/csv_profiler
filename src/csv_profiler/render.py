from __future__ import annotations

import json
from pathlib import Path

from datetime import datetime

def render_markdown(report: dict) -> str:
    lines: list[str] = []
    lines.append(f"# CSV Profiling Report\n")
    lines.append(f"Generated: {datetime.now().isoformat(timespec='seconds')}\n")
    lines.append("## Summary\n")
    lines.append(f"- Rows: **{report['n_rows']}**")
    lines.append(f"- Columns: **{report['n_cols']}**\n")
    
    lines.append("## Columns\n")
    lines.append("| name | type | missing | missing_pct | unique |")
    lines.append("|---|---:|---:|---:|---:|")
    lines.extend([
        f"| {c['name']} | {c['type']} | {c['missing']} | {c['missing_pct']:.1f}% | {c['unique']} |"
        for c in report["columns"]
    ])
    lines.append("\n## Notes\n")
    lines.append("- Missing values are: `''`, `na`, `n/a`, `null`, `none`, `nan` (case-insensitive)")
    return "\n".join(lines)


def write_json(report: dict, path: str | Path) -> None:

    path = Path(path)
    
    folder = path.parent

    if not folder.exists():
        folder.mkdir(parents=True)

    with path.open("w") as f:
        json.dump(report, f, indent=2)


def write_markdown(report: dict, path: str | Path) -> None:

    path = Path(path)
    
    folder = path.parent

    if not folder.exists():
        folder.mkdir(parents=True)
        
    with path.open("w") as f:
    
        f.write("Report")
        
        f.write(f"Rows: {report['rows']}")
        f.write(f"Columns: {len(report['columns'])}")
