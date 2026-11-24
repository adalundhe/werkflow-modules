from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_model_card_export_output_config import SageMakerModelCardExportOutputConfig


class SageMakerCreateModelCardExportJobRequest(BaseModel):
    ModelCardName: StrictStr
    ModelCardExportJobName: StrictStr
    OutputConfig: SageMakerModelCardExportOutputConfig
    ModelCardVersion: StrictInt | None = None
