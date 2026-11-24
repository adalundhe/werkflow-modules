from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class BackupPutRestoreValidationResultRequest(BaseModel):
    RestoreJobId: StrictStr
    ValidationStatus: Literal['FAILED', 'SUCCESSFUL', 'TIMED_OUT', 'VALIDATING']
    ValidationStatusMessage: StrictStr | None = None
