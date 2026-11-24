from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeBuildAutoRetryConfig(BaseModel):
    autoRetryLimit: StrictInt | None = None
    autoRetryNumber: StrictInt | None = None
    nextAutoRetry: StrictStr | None = None
    previousAutoRetry: StrictStr | None = None
