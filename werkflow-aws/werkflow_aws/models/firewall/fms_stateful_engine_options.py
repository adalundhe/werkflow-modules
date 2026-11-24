from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSStatefulEngineOptions(BaseModel):
    RuleOrder: StrictStr | None = None
    StreamExceptionPolicy: StrictStr | None = None
