from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_human_task_config import SageMakerHumanTaskConfig
from .sage_maker_labeling_job_algorithms_config import SageMakerLabelingJobAlgorithmsConfig
from .sage_maker_labeling_job_input_config import SageMakerLabelingJobInputConfig
from .sage_maker_labeling_job_output_config import SageMakerLabelingJobOutputConfig
from .sage_maker_labeling_job_stopping_conditions import SageMakerLabelingJobStoppingConditions
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateLabelingJobRequest(BaseModel):
    LabelingJobName: StrictStr
    LabelAttributeName: StrictStr
    InputConfig: SageMakerLabelingJobInputConfig
    OutputConfig: SageMakerLabelingJobOutputConfig
    RoleArn: StrictStr
    HumanTaskConfig: SageMakerHumanTaskConfig
    LabelCategoryConfigS3Uri: StrictStr | None = None
    StoppingConditions: SageMakerLabelingJobStoppingConditions | None = None
    LabelingJobAlgorithmsConfig: SageMakerLabelingJobAlgorithmsConfig | None = None
    Tags: list[SageMakerTagModel] | None = None
