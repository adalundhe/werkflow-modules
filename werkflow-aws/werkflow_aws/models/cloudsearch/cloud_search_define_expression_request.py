from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_search_expression import CloudSearchExpression


class CloudSearchDefineExpressionRequest(BaseModel):
    DomainName: StrictStr
    Expression: CloudSearchExpression
