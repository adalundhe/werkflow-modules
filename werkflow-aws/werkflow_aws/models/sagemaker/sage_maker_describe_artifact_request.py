from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeArtifactRequest(BaseModel):
    ArtifactArn: StrictStr
