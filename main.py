# -*- coding: utf-8 -*-

from typing import List, Dict, Optional
import os
from openai import OpenAI
import openai
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import json
import asyncio
from pydantic import BaseModel, RootModel


class ToolParam(BaseModel):
    name: str
    command: str
    args: List[str]


class McpClient:
    def __init__(self, param: ToolParam):
        self.session: Optional[ClientSession] = None
        self.param = param
        return

    async def connect_to_server(self):
        server_params = StdioServerParameters(
            command=self.param.command,
            args=self.param.args,
        ):
        # stdio_transport = await stdio_client(server_params)
        # reader, writer = await stdio_client(server_params)
        # self.session = ClientSession(reader, writer)
        return

    async def list_tools(self):
        # return self.session.list_tools()
        await asyncio.sleep(1)
        print("list tools1")
        return


with open("tools.json", "r") as f:
    data = json.load(f)
    param = ToolParam.model_validate(data[0])
    print(param)
    mcp = McpClient(param)

    loop = asyncio.new_event_loop()
    asyncio.run(mcp.list_tools())
    # loop.run_forever()
    # mcp.connect_to_server()
    # asyncio.main()


class WorkFlow:
    def __init__(self, base_url, api_key, model):
        self.client: OpenAI = OpenAI(
            base_url=base_url,
            api_key=api_key,
        )
        self.model = model
        self.mcphub: List[McpClient] = []
        return

    def add_tools_json(self):
        return

    def request(self, messages):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        print(response.choices[0].message.content)
        return

    def list_tools(self):
        # for client in self.mcphub:
        #     client.list_tools()
        return


def main():
    flow = WorkFlow(
        base_url="https://api.siliconflow.cn/v1",
        api_key="sk-lypqhxtegsgyikswxlaxbsotkqqwzowzxbweofoxtwqahtkq",
        model="deepseek-ai/DeepSeek-V3",
    )

    flow.request(
        [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"},
        ]
    )


if __name__ == "__main__":
    # main()
    pass
