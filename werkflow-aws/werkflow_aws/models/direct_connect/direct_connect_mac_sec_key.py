from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectMacSecKey(BaseModel):
    secretARN: StrictStr | None = None
    ckn: StrictStr | None = None
    state: StrictStr | None = None
    startOn: StrictStr | None = None
