from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTSigV4Authorization(BaseModel):
    signingRegion: StrictStr | None = None
    serviceName: StrictStr | None = None
    roleArn: StrictStr | None = None
