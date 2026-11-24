from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteKeyPairRequest(BaseModel):
    KeyName: StrictStr | None = None
    KeyPairId: StrictStr | None = None
    DryRun: StrictBool | None = None
