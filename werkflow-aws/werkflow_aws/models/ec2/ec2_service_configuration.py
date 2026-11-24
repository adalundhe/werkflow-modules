from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_private_dns_name_configuration import EC2PrivateDnsNameConfiguration
from .ec2_service_type_detail import EC2ServiceTypeDetail
from .ec2_supported_region_detail import EC2SupportedRegionDetail
from .ec2_tag_model import EC2TagModel


class EC2ServiceConfiguration(BaseModel):
    ServiceType: list[EC2ServiceTypeDetail] | None = None
    ServiceId: StrictStr | None = None
    ServiceName: StrictStr | None = None
    ServiceState: StrictStr | None = None
    AvailabilityZoneIds: list[StrictStr] | None = None
    AvailabilityZones: list[StrictStr] | None = None
    AcceptanceRequired: StrictBool | None = None
    ManagesVpcEndpoints: StrictBool | None = None
    NetworkLoadBalancerArns: list[StrictStr] | None = None
    GatewayLoadBalancerArns: list[StrictStr] | None = None
    SupportedIpAddressTypes: list[StrictStr] | None = None
    BaseEndpointDnsNames: list[StrictStr] | None = None
    PrivateDnsName: StrictStr | None = None
    PrivateDnsNameConfiguration: EC2PrivateDnsNameConfiguration | None = None
    PayerResponsibility: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    SupportedRegions: list[EC2SupportedRegionDetail] | None = None
    RemoteAccessEnabled: StrictBool | None = None
