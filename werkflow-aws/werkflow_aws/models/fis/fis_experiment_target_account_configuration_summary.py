from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISExperimentTargetAccountConfigurationSummary(BaseModel):
    roleArn: StrictStr | None = None
    accountId: StrictStr | None = None
    description: StrictStr | None = None
