from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_ipam_pool_source_resource_request import EC2IpamPoolSourceResourceRequest
from .ec2_request_ipam_resource_tag import EC2RequestIpamResourceTag
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateIpamPoolRequest(BaseModel):
    IpamScopeId: StrictStr
    AddressFamily: Literal['ipv4', 'ipv6']
    DryRun: StrictBool | None = None
    Locale: StrictStr | None = None
    SourceIpamPoolId: StrictStr | None = None
    Description: StrictStr | None = None
    AutoImport: StrictBool | None = None
    PubliclyAdvertisable: StrictBool | None = None
    AllocationMinNetmaskLength: StrictInt | None = None
    AllocationMaxNetmaskLength: StrictInt | None = None
    AllocationDefaultNetmaskLength: StrictInt | None = None
    AllocationResourceTags: list[EC2RequestIpamResourceTag] | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    ClientToken: StrictStr | None = None
    AwsService: Literal['ec2', 'global-services'] | None = None
    PublicIpSource: Literal['amazon', 'byoip'] | None = None
    SourceResource: EC2IpamPoolSourceResourceRequest | None = None
