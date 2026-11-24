from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_search_expression_status import CloudSearchExpressionStatus


class CloudSearchDefineExpressionResponse(BaseModel):
    Expression: CloudSearchExpressionStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
