from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCheckpointConfig(BaseModel):
    S3Uri: StrictStr | None = None
    LocalPath: StrictStr | None = None
