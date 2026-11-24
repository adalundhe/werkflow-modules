from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineResolvedPipelineVariable(BaseModel):
    name: StrictStr | None = None
    resolvedValue: StrictStr | None = None
