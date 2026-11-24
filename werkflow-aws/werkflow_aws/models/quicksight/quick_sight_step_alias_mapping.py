from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightStepAliasMapping(BaseModel):
    StepId: StrictStr | None = None
    StepAlias: StrictStr | None = None
