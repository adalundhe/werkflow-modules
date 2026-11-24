from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerPipelineExecutionSummary(BaseModel):
    PipelineExecutionArn: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    PipelineExecutionStatus: StrictStr | None = None
    PipelineExecutionDescription: StrictStr | None = None
    PipelineExecutionDisplayName: StrictStr | None = None
    PipelineExecutionFailureReason: StrictStr | None = None
    PipelineVersionAliases: list[StrictStr] | None = None
