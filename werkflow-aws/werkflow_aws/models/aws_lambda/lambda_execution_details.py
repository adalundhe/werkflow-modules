from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaExecutionDetails(BaseModel):
    InputPayload: StrictStr | None = None
