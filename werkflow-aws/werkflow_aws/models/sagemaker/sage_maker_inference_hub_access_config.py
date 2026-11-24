from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerInferenceHubAccessConfig(BaseModel):
    HubContentArn: StrictStr | None = None
