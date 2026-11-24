from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamAccessEndpoint(BaseModel):
    EndpointType: StrictStr | None = None
    VpceId: StrictStr | None = None
