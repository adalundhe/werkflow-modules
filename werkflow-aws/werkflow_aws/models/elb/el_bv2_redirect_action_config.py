from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2RedirectActionConfig(BaseModel):
    Protocol: StrictStr | None = None
    Port: StrictStr | None = None
    Host: StrictStr | None = None
    Path: StrictStr | None = None
    Query: StrictStr | None = None
    StatusCode: StrictStr | None = None
