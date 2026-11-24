from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class TranscribeJobExecutionSettings(BaseModel):
    AllowDeferredExecution: StrictBool | None = None
    DataAccessRoleArn: StrictStr | None = None
