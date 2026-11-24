from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerPipelineVersionSummary(BaseModel):
    PipelineArn: StrictStr | None = None
    PipelineVersionId: StrictInt | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    PipelineVersionDescription: StrictStr | None = None
    PipelineVersionDisplayName: StrictStr | None = None
    LastExecutionPipelineExecutionArn: StrictStr | None = None
    PipelineVersionAliases: list[StrictStr] | None = None
