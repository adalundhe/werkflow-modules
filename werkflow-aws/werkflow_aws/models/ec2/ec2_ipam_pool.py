from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_ipam_pool_source_resource import EC2IpamPoolSourceResource
from .ec2_ipam_resource_tag import EC2IpamResourceTag
from .ec2_tag_model import EC2TagModel


class EC2IpamPool(BaseModel):
    OwnerId: StrictStr | None = None
    IpamPoolId: StrictStr | None = None
    SourceIpamPoolId: StrictStr | None = None
    IpamPoolArn: StrictStr | None = None
    IpamScopeArn: StrictStr | None = None
    IpamScopeType: StrictStr | None = None
    IpamArn: StrictStr | None = None
    IpamRegion: StrictStr | None = None
    Locale: StrictStr | None = None
    PoolDepth: StrictInt | None = None
    State: StrictStr | None = None
    StateMessage: StrictStr | None = None
    Description: StrictStr | None = None
    AutoImport: StrictBool | None = None
    PubliclyAdvertisable: StrictBool | None = None
    AddressFamily: StrictStr | None = None
    AllocationMinNetmaskLength: StrictInt | None = None
    AllocationMaxNetmaskLength: StrictInt | None = None
    AllocationDefaultNetmaskLength: StrictInt | None = None
    AllocationResourceTags: list[EC2IpamResourceTag] | None = None
    Tags: list[EC2TagModel] | None = None
    AwsService: StrictStr | None = None
    PublicIpSource: StrictStr | None = None
    SourceResource: EC2IpamPoolSourceResource | None = None
