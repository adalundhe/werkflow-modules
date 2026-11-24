from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineRetryConfiguration(BaseModel):
    retryMode: StrictStr | None = None
