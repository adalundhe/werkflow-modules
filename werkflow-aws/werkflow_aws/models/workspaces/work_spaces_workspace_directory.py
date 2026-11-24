from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_active_directory_config import WorkSpacesActiveDirectoryConfig
from .work_spaces_certificate_based_auth_properties import WorkSpacesCertificateBasedAuthProperties
from .work_spaces_default_workspace_creation_properties import WorkSpacesDefaultWorkspaceCreationProperties
from .work_spaces_idc_config import WorkSpacesIDCConfig
from .work_spaces_microsoft_entra_config import WorkSpacesMicrosoftEntraConfig
from .work_spaces_saml_properties import WorkSpacesSamlProperties
from .work_spaces_selfservice_permissions import WorkSpacesSelfservicePermissions
from .work_spaces_streaming_properties import WorkSpacesStreamingProperties
from .work_spaces_workspace_access_properties import WorkSpacesWorkspaceAccessProperties


class WorkSpacesWorkspaceDirectory(BaseModel):
    DirectoryId: StrictStr | None = None
    Alias: StrictStr | None = None
    DirectoryName: StrictStr | None = None
    RegistrationCode: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
    DnsIpAddresses: list[StrictStr] | None = None
    DnsIpv6Addresses: list[StrictStr] | None = None
    CustomerUserName: StrictStr | None = None
    IamRoleId: StrictStr | None = None
    DirectoryType: StrictStr | None = None
    WorkspaceSecurityGroupId: StrictStr | None = None
    State: StrictStr | None = None
    WorkspaceCreationProperties: WorkSpacesDefaultWorkspaceCreationProperties | None = None
    ipGroupIds: list[StrictStr] | None = None
    WorkspaceAccessProperties: WorkSpacesWorkspaceAccessProperties | None = None
    Tenancy: StrictStr | None = None
    SelfservicePermissions: WorkSpacesSelfservicePermissions | None = None
    SamlProperties: WorkSpacesSamlProperties | None = None
    CertificateBasedAuthProperties: WorkSpacesCertificateBasedAuthProperties | None = None
    EndpointEncryptionMode: StrictStr | None = None
    MicrosoftEntraConfig: WorkSpacesMicrosoftEntraConfig | None = None
    WorkspaceDirectoryName: StrictStr | None = None
    WorkspaceDirectoryDescription: StrictStr | None = None
    UserIdentityType: StrictStr | None = None
    WorkspaceType: StrictStr | None = None
    IDCConfig: WorkSpacesIDCConfig | None = None
    ActiveDirectoryConfig: WorkSpacesActiveDirectoryConfig | None = None
    StreamingProperties: WorkSpacesStreamingProperties | None = None
    WorkspaceOsUserMode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
