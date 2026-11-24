from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudSearchDeleteExpressionRequest(BaseModel):
    DomainName: StrictStr
    ExpressionName: StrictStr
