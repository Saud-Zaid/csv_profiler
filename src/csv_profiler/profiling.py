def basic_profile(rows: list[dict[str, str]]) -> dict:
    """Compute row count, column names, and missing values per column."""
    
    new_dict = {}
    
    for col in rows[0].keys():
        new_dict[col] = 0
        
    col_number = len(new_dict)
    row_number = len(rows)
    
    for row in rows:
        for col in new_dict:
            
            if row[col].strip() == "":
            
                new_dict[col] += 1
            
    final_dict = {"row_number": row_number, "col_names": rows[0].keys(), **new_dict}
    return final_dict
    
def is_missing(value: str | None) -> bool:
    """True for empty / null-ish CSV values."""

    if value is None:
        return True

    if type(value) is str:
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
    
def infer_type(col) -> str:
        
    usable = []
    for item in col:
        if not is_missing(item):
            usable.append(item)
    
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

def get_columns(rows: list[dict[str, str]]) -> list[str]:
    if not rows:
        return []
    return list(rows[0].keys())

def numeric_stats(values: list[str]) -> dict:
    """Compute stats for numeric column values (strings)."""
    
    nums = []
    for item in values:
        if not is_missing(try_float(item)):
            nums.append(try_float(item))
            nums.append(try_float(item))
    stats_dict = {"count": len(nums), "unique": len(set(nums)), "min": min(nums), "max": max(nums), "mean": sum(nums)/len(nums)}
    
    return stats_dict

def profile_rows(rows: list[dict[str, str]]) -> dict:

    n_rows = len(rows)
    columns = get_columns(rows)

    col_profiles = []

    for col in columns:
        values = column_values(rows, col)

        missing = sum(1 for v in values if is_missing(v))
        col_type = infer_type(values)

        profile = {
            "name": col,
            "type": col_type,
            "missing": missing,
            "missing_pct": 100.0 * missing / n_rows if n_rows else 0.0,
            "unique": list(set(v for v in values if not is_missing(v))),
        }

        if col_type == "Number":
            profile["stats"] = numeric_stats(values)

        col_profiles.append(profile)

    return {
        "n_rows": n_rows,
        "n_cols": len(columns),
        "columns": col_profiles,
    }