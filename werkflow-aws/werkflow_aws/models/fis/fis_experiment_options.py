from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISExperimentOptions(BaseModel):
    accountTargeting: StrictStr | None = None
    emptyTargetResolutionMode: StrictStr | None = None
    actionsMode: StrictStr | None = None
