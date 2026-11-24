from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexCondition(BaseModel):
    expressionString: StrictStr | None = None
