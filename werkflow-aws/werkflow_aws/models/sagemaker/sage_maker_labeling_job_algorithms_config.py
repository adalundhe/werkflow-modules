from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_labeling_job_resource_config import SageMakerLabelingJobResourceConfig


class SageMakerLabelingJobAlgorithmsConfig(BaseModel):
    LabelingJobAlgorithmSpecificationArn: StrictStr | None = None
    InitialActiveLearningModelArn: StrictStr | None = None
    LabelingJobResourceConfig: SageMakerLabelingJobResourceConfig | None = None
