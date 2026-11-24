from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_processing_job import SageMakerProcessingJob
from .sage_maker_training_job import SageMakerTrainingJob
from .sage_maker_transform_job import SageMakerTransformJob


class SageMakerTrialComponentSourceDetail(BaseModel):
    SourceArn: StrictStr | None = None
    TrainingJob: SageMakerTrainingJob | None = None
    ProcessingJob: SageMakerProcessingJob | None = None
    TransformJob: SageMakerTransformJob | None = None
