from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailDeleteContainerImageRequest(BaseModel):
    serviceName: StrictStr
    image: StrictStr
