from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineActionConfiguration(BaseModel):
    configuration: dict[StrictStr, StrictStr] | None = None
