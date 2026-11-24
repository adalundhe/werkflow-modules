from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_external_authority_configuration import EC2ExternalAuthorityConfiguration


class EC2ModifyIpamScopeRequest(BaseModel):
    IpamScopeId: StrictStr
    DryRun: StrictBool | None = None
    Description: StrictStr | None = None
    ExternalAuthorityConfiguration: EC2ExternalAuthorityConfiguration | None = None
    RemoveExternalAuthorityConfiguration: StrictBool | None = None
