from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_prompt_summary import ConnectPromptSummary


class ConnectListPromptsResponse(BaseModel):
    PromptSummaryList: list[ConnectPromptSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
