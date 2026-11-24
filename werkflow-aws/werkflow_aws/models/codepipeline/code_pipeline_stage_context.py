from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineStageContext(BaseModel):
    name: StrictStr | None = None
