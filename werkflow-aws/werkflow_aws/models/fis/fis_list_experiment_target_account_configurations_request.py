from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISListExperimentTargetAccountConfigurationsRequest(BaseModel):
    experimentId: StrictStr
    nextToken: StrictStr | None = None
