from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_create_verified_access_endpoint_cidr_options import EC2CreateVerifiedAccessEndpointCidrOptions
from .ec2_create_verified_access_endpoint_eni_options import EC2CreateVerifiedAccessEndpointEniOptions
from .ec2_create_verified_access_endpoint_load_balancer_options import EC2CreateVerifiedAccessEndpointLoadBalancerOptions
from .ec2_create_verified_access_endpoint_rds_options import EC2CreateVerifiedAccessEndpointRdsOptions
from .ec2_tag_specification_model import EC2TagSpecificationModel
from .ec2_verified_access_sse_specification_request import EC2VerifiedAccessSseSpecificationRequest


class EC2CreateVerifiedAccessEndpointRequest(BaseModel):
    VerifiedAccessGroupId: StrictStr
    EndpointType: Literal['load-balancer', 'network-interface', 'rds', 'cidr']
    AttachmentType: Literal['vpc']
    DomainCertificateArn: StrictStr | None = None
    ApplicationDomain: StrictStr | None = None
    EndpointDomainPrefix: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    LoadBalancerOptions: EC2CreateVerifiedAccessEndpointLoadBalancerOptions | None = None
    NetworkInterfaceOptions: EC2CreateVerifiedAccessEndpointEniOptions | None = None
    Description: StrictStr | None = None
    PolicyDocument: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
    SseSpecification: EC2VerifiedAccessSseSpecificationRequest | None = None
    RdsOptions: EC2CreateVerifiedAccessEndpointRdsOptions | None = None
    CidrOptions: EC2CreateVerifiedAccessEndpointCidrOptions | None = None
