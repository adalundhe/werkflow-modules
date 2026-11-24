from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerTransformOutput(BaseModel):
    S3OutputPath: StrictStr | None = None
    Accept: StrictStr | None = None
    AssembleWith: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
