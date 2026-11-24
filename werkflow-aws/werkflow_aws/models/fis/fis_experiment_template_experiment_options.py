from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISExperimentTemplateExperimentOptions(BaseModel):
    accountTargeting: StrictStr | None = None
    emptyTargetResolutionMode: StrictStr | None = None
