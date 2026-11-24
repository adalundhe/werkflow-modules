from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_route53_hosted_zone_config_details import SecurityHubAwsRoute53HostedZoneConfigDetails


class SecurityHubAwsRoute53HostedZoneObjectDetails(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Config: SecurityHubAwsRoute53HostedZoneConfigDetails | None = None
