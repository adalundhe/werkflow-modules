from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .comprehend_syntax_token import ComprehendSyntaxToken


class ComprehendBatchDetectSyntaxItemResult(BaseModel):
    Index: StrictInt | None = None
    SyntaxTokens: list[ComprehendSyntaxToken] | None = None
