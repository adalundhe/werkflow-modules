from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueConditionExpression(BaseModel):
    Condition: StrictStr | None = None
    Value: StrictStr | None = None
    TargetColumn: StrictStr | None = None
