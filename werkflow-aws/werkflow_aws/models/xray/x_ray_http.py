from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class XRayHttp(BaseModel):
    HttpURL: StrictStr | None = None
    HttpStatus: StrictInt | None = None
    HttpMethod: StrictStr | None = None
    UserAgent: StrictStr | None = None
    ClientIp: StrictStr | None = None
