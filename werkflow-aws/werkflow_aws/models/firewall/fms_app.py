from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FMSApp(BaseModel):
    AppName: StrictStr | None = None
    Protocol: StrictStr | None = None
    Port: StrictInt | None = None
