from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_external_authority_configuration import EC2ExternalAuthorityConfiguration
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateIpamScopeRequest(BaseModel):
    IpamId: StrictStr
    DryRun: StrictBool | None = None
    Description: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    ClientToken: StrictStr | None = None
    ExternalAuthorityConfiguration: EC2ExternalAuthorityConfiguration | None = None
