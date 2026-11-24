from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteClusterExtensionRequest(BaseModel):
    ClusterArn: StrictStr
    ExtensionArn: StrictStr
