from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerFlowDefinitionOutputConfig(BaseModel):
    S3OutputPath: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
