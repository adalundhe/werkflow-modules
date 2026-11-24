from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_processing_output import SageMakerProcessingOutput


class SageMakerProcessingOutputConfig(BaseModel):
    Outputs: list[SageMakerProcessingOutput] | None = None
    KmsKeyId: StrictStr | None = None
