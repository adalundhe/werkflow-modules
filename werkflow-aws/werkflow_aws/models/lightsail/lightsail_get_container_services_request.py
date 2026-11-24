from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetContainerServicesRequest(BaseModel):
    serviceName: StrictStr | None = None
