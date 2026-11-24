from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerProcessingS3InputModel(BaseModel):
    S3Uri: StrictStr | None = None
    LocalPath: StrictStr | None = None
    S3DataType: StrictStr | None = None
    S3InputMode: StrictStr | None = None
    S3DataDistributionType: StrictStr | None = None
    S3CompressionType: StrictStr | None = None
