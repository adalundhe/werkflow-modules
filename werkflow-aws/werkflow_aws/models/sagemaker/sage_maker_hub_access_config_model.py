from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerHubAccessConfigModel(BaseModel):
    HubContentArn: StrictStr | None = None
