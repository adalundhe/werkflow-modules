from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSTrustedExecutionSummary(BaseModel):
    isolationMode: StrictStr | None = None
    attestationPolicyStatus: StrictStr | None = None
