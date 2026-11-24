from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_label_counters import SageMakerLabelCounters
from .sage_maker_labeling_job_input_config import SageMakerLabelingJobInputConfig
from .sage_maker_labeling_job_output import SageMakerLabelingJobOutput


class SageMakerLabelingJobSummary(BaseModel):
    LabelingJobName: StrictStr | None = None
    LabelingJobArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LabelingJobStatus: StrictStr | None = None
    LabelCounters: SageMakerLabelCounters | None = None
    WorkteamArn: StrictStr | None = None
    PreHumanTaskLambdaArn: StrictStr | None = None
    AnnotationConsolidationLambdaArn: StrictStr | None = None
    FailureReason: StrictStr | None = None
    LabelingJobOutput: SageMakerLabelingJobOutput | None = None
    InputConfig: SageMakerLabelingJobInputConfig | None = None
