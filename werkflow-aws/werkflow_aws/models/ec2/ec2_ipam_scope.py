from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_ipam_scope_external_authority_configuration import EC2IpamScopeExternalAuthorityConfiguration
from .ec2_tag_model import EC2TagModel


class EC2IpamScope(BaseModel):
    OwnerId: StrictStr | None = None
    IpamScopeId: StrictStr | None = None
    IpamScopeArn: StrictStr | None = None
    IpamArn: StrictStr | None = None
    IpamRegion: StrictStr | None = None
    IpamScopeType: StrictStr | None = None
    IsDefault: StrictBool | None = None
    Description: StrictStr | None = None
    PoolCount: StrictInt | None = None
    State: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    ExternalAuthorityConfiguration: EC2IpamScopeExternalAuthorityConfiguration | None = None
