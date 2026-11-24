from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_syntax_token import ComprehendSyntaxToken


class ComprehendDetectSyntaxResponse(BaseModel):
    SyntaxTokens: list[ComprehendSyntaxToken] | None = None
    ResponseMetadata: dict[str, Any] | None = None
