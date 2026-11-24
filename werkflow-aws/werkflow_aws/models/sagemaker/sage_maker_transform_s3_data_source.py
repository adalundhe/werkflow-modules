from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerTransformS3DataSource(BaseModel):
    S3DataType: StrictStr | None = None
    S3Uri: StrictStr | None = None
