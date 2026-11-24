from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class LightsailOrigin(BaseModel):
    name: StrictStr | None = None
    resourceType: StrictStr | None = None
    regionName: StrictStr | None = None
    protocolPolicy: StrictStr | None = None
    responseTimeout: StrictInt | None = None
    ipAddressType: StrictStr | None = None
    isPrivateOriginAccessEnabled: StrictBool | None = None
