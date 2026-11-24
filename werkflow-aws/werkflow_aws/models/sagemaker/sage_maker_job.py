from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_job_secondary_status_transition import SageMakerJobSecondaryStatusTransition
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerJob(BaseModel):
    JobName: StrictStr | None = None
    JobArn: StrictStr | None = None
    RoleArn: StrictStr | None = None
    JobCategory: StrictStr | None = None
    JobConfigSchemaVersion: StrictStr | None = None
    JobConfigDocument: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    JobStatus: StrictStr | None = None
    SecondaryStatus: StrictStr | None = None
    SecondaryStatusTransitions: list[SageMakerJobSecondaryStatusTransition] | None = None
    FailureReason: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
