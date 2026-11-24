from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerDescribePipelineRequest(BaseModel):
    PipelineName: StrictStr
    PipelineVersionId: StrictInt | None = None
    PipelineVersionAlias: StrictStr | None = None
