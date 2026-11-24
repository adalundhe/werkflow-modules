from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_private_dns_details import EC2PrivateDnsDetails
from .ec2_service_type_detail import EC2ServiceTypeDetail
from .ec2_tag_model import EC2TagModel


class EC2ServiceDetail(BaseModel):
    ServiceName: StrictStr | None = None
    ServiceId: StrictStr | None = None
    ServiceType: list[EC2ServiceTypeDetail] | None = None
    ServiceRegion: StrictStr | None = None
    AvailabilityZoneIds: list[StrictStr] | None = None
    AvailabilityZones: list[StrictStr] | None = None
    Owner: StrictStr | None = None
    BaseEndpointDnsNames: list[StrictStr] | None = None
    PrivateDnsName: StrictStr | None = None
    PrivateDnsNames: list[EC2PrivateDnsDetails] | None = None
    VpcEndpointPolicySupported: StrictBool | None = None
    AcceptanceRequired: StrictBool | None = None
    ManagesVpcEndpoints: StrictBool | None = None
    PayerResponsibility: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    PrivateDnsNameVerificationState: StrictStr | None = None
    SupportedIpAddressTypes: list[StrictStr] | None = None
