from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerPipelineSummary(BaseModel):
    PipelineArn: StrictStr | None = None
    PipelineName: StrictStr | None = None
    PipelineDisplayName: StrictStr | None = None
    PipelineDescription: StrictStr | None = None
    RoleArn: StrictStr | None = None
    CreationTime: datetime.datetime | None = None
    LastModifiedTime: datetime.datetime | None = None
    LastExecutionTime: datetime.datetime | None = None
