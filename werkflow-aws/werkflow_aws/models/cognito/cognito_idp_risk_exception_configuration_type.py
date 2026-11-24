from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPRiskExceptionConfigurationType(BaseModel):
    BlockedIPRangeList: list[StrictStr] | None = None
    SkippedIPRangeList: list[StrictStr] | None = None
