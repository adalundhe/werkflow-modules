from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAdditionalS3DataSource(BaseModel):
    S3DataType: StrictStr | None = None
    S3Uri: StrictStr | None = None
    CompressionType: StrictStr | None = None
    ETag: StrictStr | None = None
