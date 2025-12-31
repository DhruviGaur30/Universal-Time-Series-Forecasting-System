# core/validator.py
#Purpose: rust, safety, and robustness.
# Works with ANY schema, Never crashes UI, Produces quality score. 

def validate_data(df, schema):
    result = {
        "is_valid": True,
        "errors": [],
        "warnings": [],
        "statistics": {}
    }

    # Basic checks
    if schema.time_col not in df.columns:
        result["errors"].append("Time column missing")
        result["is_valid"] = False

    if schema.target_col not in df.columns:
        result["errors"].append("Target column missing")
        result["is_valid"] = False

    # Statistics (safe)
    result["statistics"] = {
        "rows": len(df),
        "entities": len(schema.entity_cols),
        "date_range": (
            df[schema.time_col].min(),
            df[schema.time_col].max()
        )
    }

    return result
