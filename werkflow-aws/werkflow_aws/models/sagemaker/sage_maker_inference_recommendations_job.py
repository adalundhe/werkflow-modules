from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerInferenceRecommendationsJob(BaseModel):
    JobName: StrictStr | None = None
    JobDescription: StrictStr | None = None
    JobType: StrictStr | None = None
    JobArn: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CompletionTime: datetime.datetime | StrictStr | None = None
    RoleArn: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    ModelName: StrictStr | None = None
    SamplePayloadUrl: StrictStr | None = None
    ModelPackageVersionArn: StrictStr | None = None
