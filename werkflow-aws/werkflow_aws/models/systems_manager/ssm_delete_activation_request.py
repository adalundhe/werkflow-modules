from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMDeleteActivationRequest(BaseModel):
    ActivationId: StrictStr
