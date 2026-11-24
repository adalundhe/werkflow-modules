from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSTrustedExecutionConfiguration(BaseModel):
    isolationMode: StrictStr | None = None
    attestationPolicy: StrictStr | None = None
