from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudSearchExpression(BaseModel):
    ExpressionName: StrictStr | None = None
    ExpressionValue: StrictStr | None = None
