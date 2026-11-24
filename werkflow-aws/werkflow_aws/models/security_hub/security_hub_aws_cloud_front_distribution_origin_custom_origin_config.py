from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_cloud_front_distribution_origin_ssl_protocols import SecurityHubAwsCloudFrontDistributionOriginSslProtocols


class SecurityHubAwsCloudFrontDistributionOriginCustomOriginConfig(BaseModel):
    HttpPort: StrictInt | None = None
    HttpsPort: StrictInt | None = None
    OriginKeepaliveTimeout: StrictInt | None = None
    OriginProtocolPolicy: StrictStr | None = None
    OriginReadTimeout: StrictInt | None = None
    OriginSslProtocols: SecurityHubAwsCloudFrontDistributionOriginSslProtocols | None = None
