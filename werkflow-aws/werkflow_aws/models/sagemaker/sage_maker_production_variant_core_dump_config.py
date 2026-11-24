from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerProductionVariantCoreDumpConfig(BaseModel):
    DestinationS3Uri: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
