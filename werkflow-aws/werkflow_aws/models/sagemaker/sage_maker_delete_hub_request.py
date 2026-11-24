from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteHubRequest(BaseModel):
    HubName: StrictStr
