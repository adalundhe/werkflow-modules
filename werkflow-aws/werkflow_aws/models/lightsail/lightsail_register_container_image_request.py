from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailRegisterContainerImageRequest(BaseModel):
    serviceName: StrictStr
    label: StrictStr
    digest: StrictStr
