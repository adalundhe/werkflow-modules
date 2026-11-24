from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LightsailInstanceMetadataOptions(BaseModel):
    state: StrictStr | None = None
    httpTokens: StrictStr | None = None
    httpEndpoint: StrictStr | None = None
    httpPutResponseHopLimit: StrictInt | None = None
    httpProtocolIpv6: StrictStr | None = None
