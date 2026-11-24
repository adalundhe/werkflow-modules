from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFScheduleLambdaFunctionDecisionAttributes(BaseModel):
    id: StrictStr
    name: StrictStr
    control: StrictStr | None = None
    input: StrictStr | None = None
    startToCloseTimeout: StrictStr | None = None
