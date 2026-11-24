from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerS3FileSystem(BaseModel):
    S3Uri: StrictStr | None = None
