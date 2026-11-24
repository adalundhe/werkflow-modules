from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_route53_hosted_zone_object_details import SecurityHubAwsRoute53HostedZoneObjectDetails
from .security_hub_aws_route53_hosted_zone_vpc_details import SecurityHubAwsRoute53HostedZoneVpcDetails
from .security_hub_aws_route53_query_logging_config_details import SecurityHubAwsRoute53QueryLoggingConfigDetails


class SecurityHubAwsRoute53HostedZoneDetails(BaseModel):
    HostedZone: SecurityHubAwsRoute53HostedZoneObjectDetails | None = None
    Vpcs: list[SecurityHubAwsRoute53HostedZoneVpcDetails] | None = None
    NameServers: list[StrictStr] | None = None
    QueryLoggingConfig: SecurityHubAwsRoute53QueryLoggingConfigDetails | None = None
