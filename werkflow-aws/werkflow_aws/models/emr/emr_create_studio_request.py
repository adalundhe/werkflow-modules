from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .emr_tag import EMRTag


class EMRCreateStudioRequest(BaseModel):
    Name: StrictStr
    AuthMode: Literal['SSO', 'IAM']
    VpcId: StrictStr
    SubnetIds: list[StrictStr]
    ServiceRole: StrictStr
    WorkspaceSecurityGroupId: StrictStr
    EngineSecurityGroupId: StrictStr
    DefaultS3Location: StrictStr
    Description: StrictStr | None = None
    UserRole: StrictStr | None = None
    IdpAuthUrl: StrictStr | None = None
    IdpRelayStateParameterName: StrictStr | None = None
    Tags: list[EMRTag] | None = None
    TrustedIdentityPropagationEnabled: StrictBool | None = None
    IdcUserAssignment: Literal['REQUIRED', 'OPTIONAL'] | None = None
    IdcInstanceArn: StrictStr | None = None
    EncryptionKeyArn: StrictStr | None = None
