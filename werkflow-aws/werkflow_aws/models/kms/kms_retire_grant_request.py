from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class KMSRetireGrantRequest(BaseModel):
    GrantToken: StrictStr | None = None
    KeyId: StrictStr | None = None
    GrantId: StrictStr | None = None
    DryRun: StrictBool | None = None
