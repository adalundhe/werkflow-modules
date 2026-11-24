from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EC2EnclaveOptions(BaseModel):
    Enabled: StrictBool | None = None
