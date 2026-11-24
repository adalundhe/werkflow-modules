from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .sage_maker_default_space_settings import SageMakerDefaultSpaceSettings
from .sage_maker_domain_settings_for_update import SageMakerDomainSettingsForUpdate
from .sage_maker_user_settings import SageMakerUserSettings


class SageMakerUpdateDomainRequest(BaseModel):
    DomainId: StrictStr
    DefaultUserSettings: SageMakerUserSettings | None = None
    DomainSettingsForUpdate: SageMakerDomainSettingsForUpdate | None = None
    AppSecurityGroupManagement: Literal['Service', 'Customer'] | None = None
    DefaultSpaceSettings: SageMakerDefaultSpaceSettings | None = None
    SubnetIds: list[StrictStr] | None = None
    AppNetworkAccessType: Literal['PublicInternetOnly', 'VpcOnly'] | None = None
    TagPropagation: Literal['ENABLED', 'DISABLED'] | None = None
    HomeEfsFileSystemCreation: Literal['Enabled', 'Disabled'] | None = None
    VpcId: StrictStr | None = None
