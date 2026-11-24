from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_catalyst_access_token_summary import CodeCatalystAccessTokenSummary


class CodeCatalystListAccessTokensResponse(BaseModel):
    items: list[CodeCatalystAccessTokenSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
