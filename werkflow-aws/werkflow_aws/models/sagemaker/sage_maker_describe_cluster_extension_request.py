from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeClusterExtensionRequest(BaseModel):
    ClusterArn: StrictStr
    ExtensionArn: StrictStr
