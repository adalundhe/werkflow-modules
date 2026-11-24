from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class IoTPutVerificationStateOnViolationRequest(BaseModel):
    violationId: StrictStr
    verificationState: Literal['FALSE_POSITIVE', 'BENIGN_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN']
    verificationStateDescription: StrictStr | None = None
