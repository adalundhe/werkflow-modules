from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_prompt import ConnectPrompt


class ConnectSearchPromptsResponse(BaseModel):
    Prompts: list[ConnectPrompt] | None = None
    NextToken: StrictStr | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
