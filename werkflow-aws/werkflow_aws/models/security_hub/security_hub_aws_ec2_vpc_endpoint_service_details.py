from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_aws_ec2_vpc_endpoint_service_service_type_details import SecurityHubAwsEc2VpcEndpointServiceServiceTypeDetails


class SecurityHubAwsEc2VpcEndpointServiceDetails(BaseModel):
    AcceptanceRequired: StrictBool | None = None
    AvailabilityZones: list[StrictStr] | None = None
    BaseEndpointDnsNames: list[StrictStr] | None = None
    ManagesVpcEndpoints: StrictBool | None = None
    GatewayLoadBalancerArns: list[StrictStr] | None = None
    NetworkLoadBalancerArns: list[StrictStr] | None = None
    PrivateDnsName: StrictStr | None = None
    ServiceId: StrictStr | None = None
    ServiceName: StrictStr | None = None
    ServiceState: StrictStr | None = None
    ServiceType: list[SecurityHubAwsEc2VpcEndpointServiceServiceTypeDetails] | None = None
