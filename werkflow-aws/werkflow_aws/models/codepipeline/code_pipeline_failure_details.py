from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CodePipelineFailureDetails(BaseModel):
    type: Literal['JobFailed', 'ConfigurationError', 'PermissionError', 'RevisionOutOfSync', 'RevisionUnavailable', 'SystemUnavailable']
    message: StrictStr
    externalExecutionId: StrictStr | None = None
