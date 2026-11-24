from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2VpcEncryptionControlExclusion(BaseModel):
    State: StrictStr | None = None
    StateMessage: StrictStr | None = None
