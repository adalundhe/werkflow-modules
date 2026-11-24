from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_front_origin_mtls_config import CloudFrontOriginMtlsConfig
from .cloud_front_origin_ssl_protocols import CloudFrontOriginSslProtocols


class CloudFrontCustomOriginConfig(BaseModel):
    HTTPPort: StrictInt | None = None
    HTTPSPort: StrictInt | None = None
    OriginProtocolPolicy: StrictStr | None = None
    OriginSslProtocols: CloudFrontOriginSslProtocols | None = None
    OriginReadTimeout: StrictInt | None = None
    OriginKeepaliveTimeout: StrictInt | None = None
    IpAddressType: StrictStr | None = None
    OriginMtlsConfig: CloudFrontOriginMtlsConfig | None = None
    OriginHttpVersion: StrictStr | None = None
