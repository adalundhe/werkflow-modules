from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListPipelineParametersForExecutionRequest(BaseModel):
    PipelineExecutionArn: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
