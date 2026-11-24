from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_processing_output_model import SageMakerProcessingOutputModel


class SageMakerProcessingOutputConfigModel(BaseModel):
    Outputs: list[SageMakerProcessingOutputModel] | None = None
    KmsKeyId: StrictStr | None = None
