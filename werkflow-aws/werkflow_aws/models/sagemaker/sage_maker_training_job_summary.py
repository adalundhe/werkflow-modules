from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_secondary_status import SageMakerSecondaryStatus
from .sage_maker_training_job_status import SageMakerTrainingJobStatus
from .sage_maker_warm_pool_status import SageMakerWarmPoolStatus


class SageMakerTrainingJobSummary(BaseModel):
    TrainingJobName: StrictStr | None = None
    TrainingJobArn: StrictStr | None = None
    CreationTime: datetime.datetime | None = None
    TrainingEndTime: datetime.datetime | None = None
    LastModifiedTime: datetime.datetime | None = None
    TrainingJobStatus: SageMakerTrainingJobStatus | None = None
    SecondaryStatus: SageMakerSecondaryStatus | None = None
    WarmPoolStatus: SageMakerWarmPoolStatus | None = None
    TrainingPlanArn: StrictStr | None = None
