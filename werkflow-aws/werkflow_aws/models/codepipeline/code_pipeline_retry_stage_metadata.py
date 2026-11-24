from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodePipelineRetryStageMetadata(BaseModel):
    autoStageRetryAttempt: StrictInt | None = None
    manualStageRetryAttempt: StrictInt | None = None
    latestRetryTrigger: StrictStr | None = None
