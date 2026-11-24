from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitRepositoryTriggerExecutionFailure(BaseModel):
    trigger: StrictStr | None = None
    failureMessage: StrictStr | None = None
