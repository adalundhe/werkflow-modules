from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelinePipelineVariableDeclaration(BaseModel):
    name: StrictStr | None = None
    defaultValue: StrictStr | None = None
    description: StrictStr | None = None
