from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAutoMLOutputDataConfig(BaseModel):
    KmsKeyId: StrictStr | None = None
    S3OutputPath: StrictStr | None = None
