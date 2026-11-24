from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsEc2InstanceMetadataOptions(BaseModel):
    HttpEndpoint: StrictStr | None = None
    HttpProtocolIpv6: StrictStr | None = None
    HttpPutResponseHopLimit: StrictInt | None = None
    HttpTokens: StrictStr | None = None
    InstanceMetadataTags: StrictStr | None = None
