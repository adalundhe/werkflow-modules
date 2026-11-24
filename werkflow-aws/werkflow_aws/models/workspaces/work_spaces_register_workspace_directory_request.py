from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .work_spaces_active_directory_config import WorkSpacesActiveDirectoryConfig
from .work_spaces_microsoft_entra_config import WorkSpacesMicrosoftEntraConfig
from .work_spaces_tag import WorkSpacesTag


class WorkSpacesRegisterWorkspaceDirectoryRequest(BaseModel):
    DirectoryId: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
    EnableSelfService: StrictBool | None = None
    Tenancy: Literal['DEDICATED', 'SHARED'] | None = None
    Tags: list[WorkSpacesTag] | None = None
    WorkspaceDirectoryName: StrictStr | None = None
    WorkspaceDirectoryDescription: StrictStr | None = None
    UserIdentityType: Literal['CUSTOMER_MANAGED', 'AWS_DIRECTORY_SERVICE', 'AWS_IAM_IDENTITY_CENTER'] | None = None
    WorkspaceOsUserMode: Literal['LOCAL_USER', 'DOMAIN_JOIN', 'ENTRA_JOIN', 'SELF_MANAGED'] | None = None
    IdcInstanceArn: StrictStr | None = None
    MicrosoftEntraConfig: WorkSpacesMicrosoftEntraConfig | None = None
    WorkspaceType: Literal['PERSONAL', 'POOLS'] | None = None
    ActiveDirectoryConfig: WorkSpacesActiveDirectoryConfig | None = None
