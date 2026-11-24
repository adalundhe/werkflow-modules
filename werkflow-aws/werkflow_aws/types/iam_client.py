from abc import ABC, abstractmethod
from typing import Any
from botocore.paginate import Paginator


class IAMClient(ABC):

    @abstractmethod
    def list_users(
        self,
        *,
        PathPrefix: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_user(
        self,
        *,
        UserName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_user(
        self,
        *,
        UserName: str,
        Path: str | None = None,
        PermissionsBoundary: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user(
        self,
        *,
        UserName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_access_keys(
        self,
        *,
        UserName: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_access_key(
        self,
        *,
        UserName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_access_key(
        self,
        *,
        AccessKeyId: str,
        UserName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_roles(
        self,
        *,
        PathPrefix: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_role(
        self,
        *,
        RoleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_role(
        self,
        *,
        RoleName: str,
        AssumeRolePolicyDocument: str,
        Path: str | None = None,
        Description: str | None = None,
        MaxSessionDuration: int | None = None,
        MaxSigninSessionDuration: int | None = None,
        PermissionsBoundary: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_role(
        self,
        *,
        RoleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_assume_role_policy(
        self,
        *,
        RoleName: str,
        PolicyDocument: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_role_policy(
        self,
        *,
        RoleName: str,
        PolicyArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_role_policy(
        self,
        *,
        RoleName: str,
        PolicyArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_attached_role_policies(
        self,
        *,
        RoleName: str,
        PathPrefix: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_role_policy(
        self,
        *,
        RoleName: str,
        PolicyName: str,
        PolicyDocument: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_role_policy(
        self,
        *,
        RoleName: str,
        PolicyName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_role_policy(
        self,
        *,
        RoleName: str,
        PolicyName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_role_policies(
        self,
        *,
        RoleName: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_policies(
        self,
        *,
        Scope: str | None = None,
        OnlyAttached: bool | None = None,
        PathPrefix: str | None = None,
        PolicyUsageFilter: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_policy(
        self,
        *,
        PolicyArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_policy_version(
        self,
        *,
        PolicyArn: str,
        VersionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_policy(
        self,
        *,
        PolicyName: str,
        PolicyDocument: str,
        Path: str | None = None,
        Description: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_policy(
        self,
        *,
        PolicyArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_policy_versions(
        self,
        *,
        PolicyArn: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_policy_version(
        self,
        *,
        PolicyArn: str,
        PolicyDocument: str,
        SetAsDefault: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_policy_version(
        self,
        *,
        PolicyArn: str,
        VersionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_groups(
        self,
        *,
        PathPrefix: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_group(
        self,
        *,
        GroupName: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_group(
        self,
        *,
        GroupName: str,
        Path: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_group(
        self,
        *,
        GroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_user_to_group(
        self,
        *,
        GroupName: str,
        UserName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_user_from_group(
        self,
        *,
        GroupName: str,
        UserName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_user_policy(
        self,
        *,
        UserName: str,
        PolicyArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_user_policy(
        self,
        *,
        UserName: str,
        PolicyArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_attached_user_policies(
        self,
        *,
        UserName: str,
        PathPrefix: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_instance_profiles(
        self,
        *,
        PathPrefix: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_instance_profile(
        self,
        *,
        InstanceProfileName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_instance_profile(
        self,
        *,
        InstanceProfileName: str,
        Path: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_instance_profile(
        self,
        *,
        InstanceProfileName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def accept_delegation_request(
        self,
        *,
        DelegationRequestId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def acquire_role(
        self,
        *,
        TemplateArn: str,
        TemplateMinorVersion: int | None = None,
        ReplacementValues: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_client_id_to_open_id_connect_provider(
        self,
        *,
        OpenIDConnectProviderArn: str,
        ClientID: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_role_to_instance_profile(
        self,
        *,
        InstanceProfileName: str,
        RoleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_delegation_request(
        self,
        *,
        DelegationRequestId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def attach_group_policy(
        self,
        *,
        GroupName: str,
        PolicyArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def change_password(
        self,
        *,
        OldPassword: str,
        NewPassword: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_account_alias(
        self,
        *,
        AccountAlias: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_delegation_request(
        self,
        *,
        Description: str,
        Permissions: dict[str, Any],
        RequestorWorkflowId: str,
        NotificationChannel: str,
        SessionDuration: int,
        OwnerAccountId: str | None = None,
        RequestMessage: str | None = None,
        RedirectUrl: str | None = None,
        OnlySendByOwner: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_login_profile(
        self,
        *,
        UserName: str | None = None,
        Password: str | None = None,
        PasswordResetRequired: bool | None = None,
        MaxSigninSessionDuration: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_open_id_connect_provider(
        self,
        *,
        Url: str,
        ClientIDList: list[str] | None = None,
        ThumbprintList: list[str] | None = None,
        Tags: list[dict[str, Any]] | None = None,
        ContextProvider: dict[str, Any] | None = None,
        IdentityCenterInstanceArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_saml_provider(
        self,
        *,
        SAMLMetadataDocument: str,
        Name: str,
        Tags: list[dict[str, Any]] | None = None,
        AssertionEncryptionMode: str | None = None,
        AddPrivateKey: str | None = None,
        ContextProvider: dict[str, Any] | None = None,
        IdentityCenterInstanceArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_service_linked_role(
        self,
        *,
        AWSServiceName: str,
        Description: str | None = None,
        CustomSuffix: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_service_specific_credential(
        self,
        *,
        UserName: str,
        ServiceName: str,
        CredentialAgeDays: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_virtual_mfa_device(
        self,
        *,
        VirtualMFADeviceName: str,
        Path: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deactivate_mfa_device(
        self,
        *,
        SerialNumber: str,
        UserName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_account_alias(
        self,
        *,
        AccountAlias: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_account_password_policy(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_group_policy(
        self,
        *,
        GroupName: str,
        PolicyName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_login_profile(
        self,
        *,
        UserName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_open_id_connect_provider(
        self,
        *,
        OpenIDConnectProviderArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_role_permissions_boundary(
        self,
        *,
        RoleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_saml_provider(
        self,
        *,
        SAMLProviderArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_ssh_public_key(
        self,
        *,
        UserName: str,
        SSHPublicKeyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_server_certificate(
        self,
        *,
        ServerCertificateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_service_linked_role(
        self,
        *,
        RoleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_service_specific_credential(
        self,
        *,
        ServiceSpecificCredentialId: str,
        UserName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_signing_certificate(
        self,
        *,
        CertificateId: str,
        UserName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user_permissions_boundary(
        self,
        *,
        UserName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user_policy(
        self,
        *,
        UserName: str,
        PolicyName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_virtual_mfa_device(
        self,
        *,
        SerialNumber: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def detach_group_policy(
        self,
        *,
        GroupName: str,
        PolicyArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_organizations_root_credentials_management(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_organizations_root_sessions(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def disable_outbound_web_identity_federation(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_mfa_device(
        self,
        *,
        UserName: str,
        SerialNumber: str,
        AuthenticationCode1: str,
        AuthenticationCode2: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_organizations_root_credentials_management(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_organizations_root_sessions(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def enable_outbound_web_identity_federation(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_credential_report(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_organizations_access_report(
        self,
        *,
        EntityPath: str,
        OrganizationsPolicyId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def generate_service_last_accessed_details(
        self,
        *,
        Arn: str,
        Granularity: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_access_key_last_used(
        self,
        *,
        AccessKeyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_account_authorization_details(
        self,
        *,
        Filter: list[str] | None = None,
        MaxItems: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_account_password_policy(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_account_properties(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_account_summary(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_context_keys_for_custom_policy(
        self,
        *,
        PolicyInputList: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_context_keys_for_principal_policy(
        self,
        *,
        PolicySourceArn: str,
        PolicyInputList: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_credential_report(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_delegation_request(
        self,
        *,
        DelegationRequestId: str,
        DelegationPermissionCheck: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_group_policy(
        self,
        *,
        GroupName: str,
        PolicyName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_human_readable_summary(
        self,
        *,
        EntityArn: str,
        Locale: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_login_profile(
        self,
        *,
        UserName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_mfa_device(
        self,
        *,
        SerialNumber: str,
        UserName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_open_id_connect_provider(
        self,
        *,
        OpenIDConnectProviderArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_organizations_access_report(
        self,
        *,
        JobId: str,
        MaxItems: int | None = None,
        Marker: str | None = None,
        SortKey: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_outbound_web_identity_federation_info(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_role_template_version(
        self,
        *,
        TemplateArn: str,
        MinorVersion: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_saml_provider(
        self,
        *,
        SAMLProviderArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ssh_public_key(
        self,
        *,
        UserName: str,
        SSHPublicKeyId: str,
        Encoding: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_server_certificate(
        self,
        *,
        ServerCertificateName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_service_last_accessed_details(
        self,
        *,
        JobId: str,
        MaxItems: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_service_last_accessed_details_with_entities(
        self,
        *,
        JobId: str,
        ServiceNamespace: str,
        MaxItems: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_service_linked_role_deletion_status(
        self,
        *,
        DeletionTaskId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_user_policy(
        self,
        *,
        UserName: str,
        PolicyName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_account_aliases(
        self,
        *,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_attached_group_policies(
        self,
        *,
        GroupName: str,
        PathPrefix: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_delegation_requests(
        self,
        *,
        OwnerId: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_entities_for_policy(
        self,
        *,
        PolicyArn: str,
        EntityFilter: str | None = None,
        PathPrefix: str | None = None,
        PolicyUsageFilter: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_group_policies(
        self,
        *,
        GroupName: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_groups_for_user(
        self,
        *,
        UserName: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_instance_profile_tags(
        self,
        *,
        InstanceProfileName: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_instance_profiles_for_role(
        self,
        *,
        RoleName: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_mfa_device_tags(
        self,
        *,
        SerialNumber: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_mfa_devices(
        self,
        *,
        UserName: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_open_id_connect_provider_tags(
        self,
        *,
        OpenIDConnectProviderArn: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_open_id_connect_providers(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_organizations_features(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_policies_granting_service_access(
        self,
        *,
        Arn: str,
        ServiceNamespaces: list[str],
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_policy_tags(
        self,
        *,
        PolicyArn: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_role_tags(
        self,
        *,
        RoleName: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_saml_provider_tags(
        self,
        *,
        SAMLProviderArn: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_saml_providers(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_ssh_public_keys(
        self,
        *,
        UserName: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_server_certificate_tags(
        self,
        *,
        ServerCertificateName: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_server_certificates(
        self,
        *,
        PathPrefix: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_service_specific_credentials(
        self,
        *,
        UserName: str | None = None,
        ServiceName: str | None = None,
        AllUsers: bool | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_signing_certificates(
        self,
        *,
        UserName: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_user_policies(
        self,
        *,
        UserName: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_user_tags(
        self,
        *,
        UserName: str,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_virtual_mfa_devices(
        self,
        *,
        AssignmentStatus: str | None = None,
        Marker: str | None = None,
        MaxItems: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_account_properties(
        self,
        *,
        Properties: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_group_policy(
        self,
        *,
        GroupName: str,
        PolicyName: str,
        PolicyDocument: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_role_permissions_boundary(
        self,
        *,
        RoleName: str,
        PermissionsBoundary: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_user_permissions_boundary(
        self,
        *,
        UserName: str,
        PermissionsBoundary: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_user_policy(
        self,
        *,
        UserName: str,
        PolicyName: str,
        PolicyDocument: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reject_delegation_request(
        self,
        *,
        DelegationRequestId: str,
        Notes: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_client_id_from_open_id_connect_provider(
        self,
        *,
        OpenIDConnectProviderArn: str,
        ClientID: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def remove_role_from_instance_profile(
        self,
        *,
        InstanceProfileName: str,
        RoleName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def reset_service_specific_credential(
        self,
        *,
        ServiceSpecificCredentialId: str,
        UserName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def resync_mfa_device(
        self,
        *,
        UserName: str,
        SerialNumber: str,
        AuthenticationCode1: str,
        AuthenticationCode2: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def send_delegation_token(
        self,
        *,
        DelegationRequestId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_default_policy_version(
        self,
        *,
        PolicyArn: str,
        VersionId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_security_token_service_preferences(
        self,
        *,
        GlobalEndpointTokenVersion: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def simulate_custom_policy(
        self,
        *,
        PolicyInputList: list[str],
        ActionNames: list[str],
        PermissionsBoundaryPolicyInputList: list[str] | None = None,
        OrderedOrganizationPolicyInputList: list[dict[str, Any]] | None = None,
        ResourceArns: list[str] | None = None,
        ResourcePolicy: str | None = None,
        ResourceOwner: str | None = None,
        CallerArn: str | None = None,
        ContextEntries: list[dict[str, Any]] | None = None,
        ResourceHandlingOption: str | None = None,
        MaxItems: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def simulate_principal_policy(
        self,
        *,
        PolicySourceArn: str,
        ActionNames: list[str],
        PolicyInputList: list[str] | None = None,
        PermissionsBoundaryPolicyInputList: list[str] | None = None,
        PolicyExclusionList: list[dict[str, Any]] | None = None,
        ResourceArns: list[str] | None = None,
        ResourcePolicy: str | None = None,
        ResourceOwner: str | None = None,
        CallerArn: str | None = None,
        ContextEntries: list[dict[str, Any]] | None = None,
        ResourceHandlingOption: str | None = None,
        MaxItems: int | None = None,
        Marker: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_instance_profile(
        self,
        *,
        InstanceProfileName: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_mfa_device(
        self,
        *,
        SerialNumber: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_open_id_connect_provider(
        self,
        *,
        OpenIDConnectProviderArn: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_policy(
        self,
        *,
        PolicyArn: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_role(
        self,
        *,
        RoleName: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_saml_provider(
        self,
        *,
        SAMLProviderArn: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_server_certificate(
        self,
        *,
        ServerCertificateName: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_user(
        self,
        *,
        UserName: str,
        Tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_instance_profile(
        self,
        *,
        InstanceProfileName: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_mfa_device(
        self,
        *,
        SerialNumber: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_open_id_connect_provider(
        self,
        *,
        OpenIDConnectProviderArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_policy(
        self,
        *,
        PolicyArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_role(
        self,
        *,
        RoleName: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_saml_provider(
        self,
        *,
        SAMLProviderArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_server_certificate(
        self,
        *,
        ServerCertificateName: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_user(
        self,
        *,
        UserName: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_access_key(
        self,
        *,
        AccessKeyId: str,
        Status: str,
        UserName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_account_password_policy(
        self,
        *,
        MinimumPasswordLength: int | None = None,
        RequireSymbols: bool | None = None,
        RequireNumbers: bool | None = None,
        RequireUppercaseCharacters: bool | None = None,
        RequireLowercaseCharacters: bool | None = None,
        AllowUsersToChangePassword: bool | None = None,
        MaxPasswordAge: int | None = None,
        PasswordReusePrevention: int | None = None,
        HardExpiry: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_delegation_request(
        self,
        *,
        DelegationRequestId: str,
        Notes: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_group(
        self,
        *,
        GroupName: str,
        NewPath: str | None = None,
        NewGroupName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_login_profile(
        self,
        *,
        UserName: str,
        Password: str | None = None,
        PasswordResetRequired: bool | None = None,
        MaxSigninSessionDuration: int | None = None,
        ResetMaxSigninSessionDuration: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_open_id_connect_provider(
        self,
        *,
        OpenIDConnectProviderArn: str,
        ContextProvider: dict[str, Any] | None = None,
        IdentityCenterInstanceArn: str | None = None,
        RemoveContextProvider: bool | None = None,
        RemoveIdentityCenterInstance: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_open_id_connect_provider_thumbprint(
        self,
        *,
        OpenIDConnectProviderArn: str,
        ThumbprintList: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_role(
        self,
        *,
        RoleName: str,
        Description: str | None = None,
        MaxSessionDuration: int | None = None,
        MaxSigninSessionDuration: int | None = None,
        ResetMaxSigninSessionDuration: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_role_description(
        self,
        *,
        RoleName: str,
        Description: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_saml_provider(
        self,
        *,
        SAMLProviderArn: str,
        SAMLMetadataDocument: str | None = None,
        AssertionEncryptionMode: str | None = None,
        AddPrivateKey: str | None = None,
        RemovePrivateKey: str | None = None,
        ContextProvider: dict[str, Any] | None = None,
        IdentityCenterInstanceArn: str | None = None,
        RemoveContextProvider: bool | None = None,
        RemoveIdentityCenterInstance: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_ssh_public_key(
        self,
        *,
        UserName: str,
        SSHPublicKeyId: str,
        Status: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_server_certificate(
        self,
        *,
        ServerCertificateName: str,
        NewPath: str | None = None,
        NewServerCertificateName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_service_specific_credential(
        self,
        *,
        ServiceSpecificCredentialId: str,
        Status: str,
        UserName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_signing_certificate(
        self,
        *,
        CertificateId: str,
        Status: str,
        UserName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user(
        self,
        *,
        UserName: str,
        NewPath: str | None = None,
        NewUserName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def upload_ssh_public_key(
        self,
        *,
        UserName: str,
        SSHPublicKeyBody: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def upload_server_certificate(
        self,
        *,
        ServerCertificateName: str,
        CertificateBody: str,
        PrivateKey: str,
        Path: str | None = None,
        CertificateChain: str | None = None,
        Tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def upload_signing_certificate(
        self,
        *,
        CertificateBody: str,
        UserName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
