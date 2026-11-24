from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2EncryptionSupport(BaseModel):
    EncryptionState: StrictStr | None = None
    StateMessage: StrictStr | None = None
