from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerCreateModelBiasJobDefinitionResponse(BaseModel):
    JobDefinitionArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
