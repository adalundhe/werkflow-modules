from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .sage_maker_default_space_settings import SageMakerDefaultSpaceSettings
from .sage_maker_domain_settings import SageMakerDomainSettings
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_user_settings import SageMakerUserSettings


class SageMakerCreateDomainRequest(BaseModel):
    DomainName: StrictStr
    AuthMode: Literal['SSO', 'IAM']
    DefaultUserSettings: SageMakerUserSettings
    DomainSettings: SageMakerDomainSettings | None = None
    SubnetIds: list[StrictStr] | None = None
    VpcId: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
    AppNetworkAccessType: Literal['PublicInternetOnly', 'VpcOnly'] | None = None
    HomeEfsFileSystemKmsKeyId: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    AppSecurityGroupManagement: Literal['Service', 'Customer'] | None = None
    HomeEfsFileSystemCreation: Literal['Enabled', 'Disabled'] | None = None
    TagPropagation: Literal['ENABLED', 'DISABLED'] | None = None
    DefaultSpaceSettings: SageMakerDefaultSpaceSettings | None = None
