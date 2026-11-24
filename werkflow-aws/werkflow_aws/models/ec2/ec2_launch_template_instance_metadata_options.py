from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2LaunchTemplateInstanceMetadataOptions(BaseModel):
    State: StrictStr | None = None
    HttpTokens: StrictStr | None = None
    HttpPutResponseHopLimit: StrictInt | None = None
    HttpEndpoint: StrictStr | None = None
    HttpProtocolIpv6: StrictStr | None = None
    InstanceMetadataTags: StrictStr | None = None
