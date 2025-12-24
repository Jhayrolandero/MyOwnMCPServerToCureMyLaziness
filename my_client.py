import asyncio
from fastmcp import Client
from dotenv import load_dotenv
import os

load_dotenv()
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

client = Client("https://sure-amethyst-turkey.fastmcp.app/mcp")

async def call_tools(name: str):
    async with client:
        response = await client.call_tool("greet", {"name": name})
        print(response)
        

asyncio.run(call_tools("Alice"))