from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerPipelineDefinitionS3Location(BaseModel):
    Bucket: StrictStr
    ObjectKey: StrictStr
    VersionId: StrictStr | None = None
