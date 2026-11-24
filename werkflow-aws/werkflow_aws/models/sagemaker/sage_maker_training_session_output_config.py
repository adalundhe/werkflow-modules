from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_training_session_s3_location import SageMakerTrainingSessionS3Location


class SageMakerTrainingSessionOutputConfig(BaseModel):
    S3Location: SageMakerTrainingSessionS3Location | None = None
