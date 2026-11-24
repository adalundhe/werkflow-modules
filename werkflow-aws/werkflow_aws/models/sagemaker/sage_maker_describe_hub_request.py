from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeHubRequest(BaseModel):
    HubName: StrictStr
