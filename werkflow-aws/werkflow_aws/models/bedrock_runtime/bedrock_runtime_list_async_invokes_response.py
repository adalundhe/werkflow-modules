from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_async_invoke_summary import BedrockRuntimeAsyncInvokeSummary


class BedrockRuntimeListAsyncInvokesResponse(BaseModel):
    nextToken: StrictStr | None = None
    asyncInvokeSummaries: list[BedrockRuntimeAsyncInvokeSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
