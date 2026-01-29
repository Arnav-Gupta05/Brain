from database import get_connection


def tool_save_memory(key: str, value: str) -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO memory (key, value)
        VALUES (?, ?)
        ON CONFLICT(key) DO UPDATE SET value=excluded.value
    """, (key, value))

    conn.commit()
    conn.close()

    return {"key": key, "value": value}


def tool_get_memory(key: str) -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT value FROM memory WHERE key = ?", (key,))
    row = cursor.fetchone()

    conn.close()

    if row:
        return {"key": key, "value": row["value"]}
    else:
        return {"error": "Key not found in memory"}


