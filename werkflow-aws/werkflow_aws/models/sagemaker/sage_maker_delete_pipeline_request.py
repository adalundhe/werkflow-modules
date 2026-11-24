from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeletePipelineRequest(BaseModel):
    PipelineName: StrictStr
    ClientRequestToken: StrictStr
