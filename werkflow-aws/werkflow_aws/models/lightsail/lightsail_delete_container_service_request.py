from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailDeleteContainerServiceRequest(BaseModel):
    serviceName: StrictStr
