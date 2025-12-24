import asyncio
from fastmcp import Client

client = Client("http://localhost:8000/mcp")

async def call_tools(name: str):
    async with client:
        response = await client.call_tool("greet", {"name": name})
        print(response)
        

asyncio.run(call_tools("Alice"))