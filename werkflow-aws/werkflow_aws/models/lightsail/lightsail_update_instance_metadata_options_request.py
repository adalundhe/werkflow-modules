from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class LightsailUpdateInstanceMetadataOptionsRequest(BaseModel):
    instanceName: StrictStr
    httpTokens: Literal['optional', 'required'] | None = None
    httpEndpoint: Literal['disabled', 'enabled'] | None = None
    httpPutResponseHopLimit: StrictInt | None = None
    httpProtocolIpv6: Literal['disabled', 'enabled'] | None = None
