from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerOutputDataConfigModel(BaseModel):
    KmsKeyId: StrictStr | None = None
    S3OutputPath: StrictStr | None = None
    CompressionType: StrictStr | None = None
