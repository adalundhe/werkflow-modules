from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodeBuildStartCommandExecutionRequest(BaseModel):
    sandboxId: StrictStr
    command: StrictStr
    type: Literal['SHELL'] | None = None
