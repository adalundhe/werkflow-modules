from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxStartMisconfiguredStateRecoveryRequest(BaseModel):
    FileSystemId: StrictStr
    ClientRequestToken: StrictStr | None = None
