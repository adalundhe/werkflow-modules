from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_prompt import ConnectPrompt


class ConnectDescribePromptResponse(BaseModel):
    Prompt: ConnectPrompt | None = None
    ResponseMetadata: dict[str, Any] | None = None
