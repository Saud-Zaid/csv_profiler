def is_missing(value: str | None) -> bool:
    """True for empty / null-ish CSV values."""

    if value is None:
        return True
        
    if type(value) == str:
        value = value.strip().lower()

    match value:
        case "" | "na" | "n/a" | "null" | "none" | "nan":
            return True
        case _:
            return False

def try_float(value: str) -> float | None:
    """Return float(value) or None if it fails"""
        
    try:
        return float(value)
    except: return None
    
from datetime import datetime

def md_header(source: str) -> list[str]:
    """Return lines for the top of the report"""
    
    lines = []
    
    lines.append("# CSV Profile Report")
    
    lines.append(f"Source: {source}")
    
    lines.append(f"Generated at: {datetime.now().isoformat(timespec='seconds')}")
    
    return lines
    
from datetime import datetime

def md_table_header(source: str) -> list[str]:
    """Return lines for the top of the report"""
    
    return [
        "| Column | Type | Missing | Unique |",
        "|---|---:|---:|---:|",
    ]
    
def md_col_row(name: str, typ: str, missing: int, missing_pct: float, unique: int) -> str:
    return f"| {name} | {typ} | {missing} ({missing_pct:.1%}) | {unique} |"
    

    
def md_bullets(items: list[str]) -> list[str]:
    """Turn ['a', 'b'] into ['- a', '- b']"""
    
    for i in range(len(items)):
        items[i] = "- " + items[i]
        
    return items
    
def get_columns(rows: list[dict[str, str]]) -> list[str]:
    if not rows:
        return []
    return list(rows[0].keys())
    
def infer_type(col) -> str:
        
    usable = []
    for item in col:
        if not is_missing(item):
            usable.append(item)
    
    if not usable:
        return "Text"
    
    for item in usable:
        if type(try_float(item)) is not float:
            if try_float(item) is None:
                return "Text"
    return "Number"
    
def column_values(rows: list[dict[str, str]], col:str) -> list[str]:
    
    valuesOfColumn = []
    for row in rows:
        valuesOfColumn.append(row.get(col, ""))
    
    return valuesOfColumn
    
def numeric_stats(values: list[str]) -> dict:
    """Compute stats for numeric column values (strings)."""
    
    nums = []
    for item in values:
        if not is_missing(try_float(item)):
            nums.append(try_float(item))
            nums.append(try_float(item))
    stats_dict = {"count": len(nums), "unique": len(set(nums)), "min": min(nums), "max": max(nums), "mean": sum(nums)/len(nums)}
    
    return stats_dict