from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_origin_ssl_protocols import CloudFrontOriginSslProtocols


class CloudFrontVpcOriginEndpointConfig(BaseModel):
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    HTTPPort: StrictInt | None = None
    HTTPSPort: StrictInt | None = None
    OriginProtocolPolicy: StrictStr | None = None
    OriginSslProtocols: CloudFrontOriginSslProtocols | None = None
    IpAddressType: StrictStr | None = None
