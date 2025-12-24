from fastmcp import FastMCP

mcp = FastMCP("My MCP Server", auth=None)


@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)