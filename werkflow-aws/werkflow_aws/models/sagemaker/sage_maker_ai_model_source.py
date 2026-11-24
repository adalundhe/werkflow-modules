from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_ai_model_source_s3 import SageMakerAIModelSourceS3


class SageMakerAIModelSource(BaseModel):
    S3: SageMakerAIModelSourceS3 | None = None
