from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerInferenceHubAccessConfigModel(BaseModel):
    HubContentArn: StrictStr | None = None
