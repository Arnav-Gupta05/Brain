# app/tools/calculator.py

def tool_calculate(expression: str) -> dict:
    """
    Evaluates a simple mathematical expression string.

    Example:
        "5 * (10 + 2)" -> 60

    NOTE:
    This uses Python's eval(). Security risks are documented in README.
    """

    try:
        # Restrict eval environment (very important)
        allowed_globals = {"__builtins__": None}
        result = eval(expression, allowed_globals, {})

        return {"result": result}

    except Exception as e:
        return {"error": f"Invalid expression: {str(e)}"}


