from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineS3ArtifactLocation(BaseModel):
    bucketName: StrictStr | None = None
    objectKey: StrictStr | None = None
