from __future__ import annotations
from pydantic import BaseModel
from .cloud_search_expression import CloudSearchExpression
from .cloud_search_option_status import CloudSearchOptionStatus


class CloudSearchExpressionStatus(BaseModel):
    Options: CloudSearchExpression | None = None
    Status: CloudSearchOptionStatus | None = None
