from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildBatchGetCommandExecutionsRequest(BaseModel):
    sandboxId: StrictStr
    commandExecutionIds: list[StrictStr]
