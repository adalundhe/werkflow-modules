from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteWorkteamRequest(BaseModel):
    WorkteamName: StrictStr
