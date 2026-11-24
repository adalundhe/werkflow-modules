from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerUpdatePipelineVersionResponse(BaseModel):
    PipelineArn: StrictStr | None = None
    PipelineVersionId: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
