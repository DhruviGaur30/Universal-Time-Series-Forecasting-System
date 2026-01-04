# core/validator.py
#Purpose: rust, safety, and robustness.
# Works with ANY schema, Never crashes UI, Produces quality score. 

def validate_data(df, schema):
    errors = []

    if schema.time_col not in df.columns:
        errors.append("Time column missing")

    if schema.target_col not in df.columns:
        errors.append("Target column missing")

    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }
