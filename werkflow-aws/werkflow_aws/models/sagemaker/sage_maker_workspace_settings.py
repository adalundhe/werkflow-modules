from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerWorkspaceSettings(BaseModel):
    S3ArtifactPath: StrictStr | None = None
    S3KmsKeyId: StrictStr | None = None
