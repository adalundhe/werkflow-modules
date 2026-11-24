from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraExperienceEndpoint(BaseModel):
    EndpointType: StrictStr | None = None
    Endpoint: StrictStr | None = None
