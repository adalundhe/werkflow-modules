from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerEdgePackagingJobSummary(BaseModel):
    EdgePackagingJobArn: StrictStr | None = None
    EdgePackagingJobName: StrictStr | None = None
    EdgePackagingJobStatus: StrictStr | None = None
    CompilationJobName: StrictStr | None = None
    ModelName: StrictStr | None = None
    ModelVersion: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
