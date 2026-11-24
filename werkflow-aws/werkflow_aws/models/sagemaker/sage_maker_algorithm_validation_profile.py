from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_training_job_definition import SageMakerTrainingJobDefinition
from .sage_maker_transform_job_definition import SageMakerTransformJobDefinition


class SageMakerAlgorithmValidationProfile(BaseModel):
    ProfileName: StrictStr | None = None
    TrainingJobDefinition: SageMakerTrainingJobDefinition | None = None
    TransformJobDefinition: SageMakerTransformJobDefinition | None = None
