from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeWorkteamRequest(BaseModel):
    WorkteamName: StrictStr
