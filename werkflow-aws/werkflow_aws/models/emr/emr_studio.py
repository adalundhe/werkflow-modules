from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .emr_tag import EMRTag


class EMRStudio(BaseModel):
    StudioId: StrictStr | None = None
    StudioArn: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    AuthMode: StrictStr | None = None
    VpcId: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
    ServiceRole: StrictStr | None = None
    UserRole: StrictStr | None = None
    WorkspaceSecurityGroupId: StrictStr | None = None
    EngineSecurityGroupId: StrictStr | None = None
    Url: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    DefaultS3Location: StrictStr | None = None
    IdpAuthUrl: StrictStr | None = None
    IdpRelayStateParameterName: StrictStr | None = None
    Tags: list[EMRTag] | None = None
    IdcInstanceArn: StrictStr | None = None
    TrustedIdentityPropagationEnabled: StrictBool | None = None
    IdcUserAssignment: StrictStr | None = None
    EncryptionKeyArn: StrictStr | None = None
