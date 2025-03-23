# -*- coding: utf-8 -*-

from typing import List, Dict, Optional
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("TestDemo")


@mcp.tool()
def get_weather(city: str) -> str:
    "获取城市的天气信息"
    print(f"city {city}")
    return "晴朗"
