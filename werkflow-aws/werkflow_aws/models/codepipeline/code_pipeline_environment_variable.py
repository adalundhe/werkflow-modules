from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineEnvironmentVariable(BaseModel):
    name: StrictStr | None = None
    value: StrictStr | None = None
    type: StrictStr | None = None
