from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_human_task_config import SageMakerHumanTaskConfig
from .sage_maker_label_counters import SageMakerLabelCounters
from .sage_maker_labeling_job_algorithms_config import SageMakerLabelingJobAlgorithmsConfig
from .sage_maker_labeling_job_input_config import SageMakerLabelingJobInputConfig
from .sage_maker_labeling_job_output import SageMakerLabelingJobOutput
from .sage_maker_labeling_job_output_config import SageMakerLabelingJobOutputConfig
from .sage_maker_labeling_job_stopping_conditions import SageMakerLabelingJobStoppingConditions
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerDescribeLabelingJobResponse(BaseModel):
    LabelingJobStatus: StrictStr | None = None
    LabelCounters: SageMakerLabelCounters | None = None
    FailureReason: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    JobReferenceCode: StrictStr | None = None
    LabelingJobName: StrictStr | None = None
    LabelingJobArn: StrictStr | None = None
    LabelAttributeName: StrictStr | None = None
    InputConfig: SageMakerLabelingJobInputConfig | None = None
    OutputConfig: SageMakerLabelingJobOutputConfig | None = None
    RoleArn: StrictStr | None = None
    LabelCategoryConfigS3Uri: StrictStr | None = None
    StoppingConditions: SageMakerLabelingJobStoppingConditions | None = None
    LabelingJobAlgorithmsConfig: SageMakerLabelingJobAlgorithmsConfig | None = None
    HumanTaskConfig: SageMakerHumanTaskConfig | None = None
    Tags: list[SageMakerTagModel] | None = None
    LabelingJobOutput: SageMakerLabelingJobOutput | None = None
    ResponseMetadata: dict[str, Any] | None = None
