from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerHubContentStepMetadata(BaseModel):
    HubArn: StrictStr | None = None
    HubContentArn: StrictStr | None = None
