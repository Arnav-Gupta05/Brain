from langchain_tools import execute_tool

print(execute_tool("calculator", "10 + 5"))
print(execute_tool("memory_save", {"key": "cat's name", "value": "Fluffy"}))
print(execute_tool("memory_read", {"key": "cat's name"}))
