from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISGetExperimentTargetAccountConfigurationRequest(BaseModel):
    experimentId: StrictStr
    accountId: StrictStr
