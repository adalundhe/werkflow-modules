from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .sage_maker_processing_instance_type import SageMakerProcessingInstanceType


class SageMakerProcessingInstancePreference(BaseModel):
    InstanceType: SageMakerProcessingInstanceType | None = None
    InstanceCount: StrictInt | None = None
