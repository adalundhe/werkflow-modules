from abc import ABC, abstractmethod
import datetime
from typing import Any, BinaryIO
from botocore.paginate import Paginator


class CognitoIDPClient(ABC):

    @abstractmethod
    def add_custom_attributes(
        self,
        *,
        UserPoolId: str,
        CustomAttributes: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def add_user_pool_client_secret(
        self,
        *,
        UserPoolId: str,
        ClientId: str,
        ClientSecret: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_add_user_to_group(
        self,
        *,
        UserPoolId: str,
        Username: str,
        GroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_confirm_sign_up(
        self,
        *,
        UserPoolId: str,
        Username: str,
        ClientMetadata: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_create_user(
        self,
        *,
        UserPoolId: str,
        Username: str,
        UserAttributes: list[dict[str, Any]] | None = None,
        ValidationData: list[dict[str, Any]] | None = None,
        TemporaryPassword: str | None = None,
        ForceAliasCreation: bool | None = None,
        MessageAction: str | None = None,
        DesiredDeliveryMediums: list[str] | None = None,
        ClientMetadata: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_delete_software_token(
        self,
        *,
        UserPoolId: str,
        Username: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_delete_user(
        self,
        *,
        UserPoolId: str,
        Username: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_delete_user_attributes(
        self,
        *,
        UserPoolId: str,
        Username: str,
        UserAttributeNames: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_disable_provider_for_user(
        self,
        *,
        UserPoolId: str,
        User: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_disable_user(
        self,
        *,
        UserPoolId: str,
        Username: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_enable_user(
        self,
        *,
        UserPoolId: str,
        Username: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_forget_device(
        self,
        *,
        UserPoolId: str,
        Username: str,
        DeviceKey: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_get_device(
        self,
        *,
        DeviceKey: str,
        UserPoolId: str,
        Username: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_get_user(
        self,
        *,
        UserPoolId: str,
        Username: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_get_user_auth_factors(
        self,
        *,
        UserPoolId: str,
        Username: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_initiate_auth(
        self,
        *,
        UserPoolId: str,
        ClientId: str,
        AuthFlow: str,
        AuthParameters: dict[str, str] | None = None,
        ClientMetadata: dict[str, str] | None = None,
        AnalyticsMetadata: dict[str, Any] | None = None,
        ContextData: dict[str, Any] | None = None,
        Session: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_link_provider_for_user(
        self,
        *,
        UserPoolId: str,
        DestinationUser: dict[str, Any],
        SourceUser: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_list_devices(
        self,
        *,
        UserPoolId: str,
        Username: str,
        Limit: int | None = None,
        PaginationToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_list_groups_for_user(
        self,
        *,
        Username: str,
        UserPoolId: str,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_list_user_auth_events(
        self,
        *,
        UserPoolId: str,
        Username: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_list_user_sessions(
        self,
        *,
        UserPoolId: str,
        Username: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_remove_user_from_group(
        self,
        *,
        UserPoolId: str,
        Username: str,
        GroupName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_reset_user_password(
        self,
        *,
        UserPoolId: str,
        Username: str,
        ClientMetadata: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_respond_to_auth_challenge(
        self,
        *,
        UserPoolId: str,
        ClientId: str,
        ChallengeName: str,
        ChallengeResponses: dict[str, str] | None = None,
        Session: str | None = None,
        AnalyticsMetadata: dict[str, Any] | None = None,
        ContextData: dict[str, Any] | None = None,
        ClientMetadata: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_revoke_user_session(
        self,
        *,
        UserPoolId: str,
        Username: str,
        SessionId: str,
        RevokeAssociatedSessions: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_set_user_mfa_preference(
        self,
        *,
        Username: str,
        UserPoolId: str,
        SMSMfaSettings: dict[str, Any] | None = None,
        SoftwareTokenMfaSettings: dict[str, Any] | None = None,
        EmailMfaSettings: dict[str, Any] | None = None,
        WebAuthnMfaSettings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_set_user_password(
        self,
        *,
        UserPoolId: str,
        Username: str,
        Password: str,
        Permanent: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_set_user_settings(
        self,
        *,
        UserPoolId: str,
        Username: str,
        MFAOptions: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_update_auth_event_feedback(
        self,
        *,
        UserPoolId: str,
        Username: str,
        EventId: str,
        FeedbackValue: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_update_device_status(
        self,
        *,
        UserPoolId: str,
        Username: str,
        DeviceKey: str,
        DeviceRememberedStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_update_user_attributes(
        self,
        *,
        UserPoolId: str,
        Username: str,
        UserAttributes: list[dict[str, Any]],
        ClientMetadata: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def admin_user_global_sign_out(
        self,
        *,
        UserPoolId: str,
        Username: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def associate_software_token(
        self,
        *,
        AccessToken: str | None = None,
        Session: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def cancel_point_in_time_recovery(
        self,
        *,
        UserPoolId: str,
        RestoreId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def change_password(
        self,
        *,
        ProposedPassword: str,
        AccessToken: str,
        PreviousPassword: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def complete_web_authn_registration(
        self,
        *,
        AccessToken: str,
        Credential: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def confirm_device(
        self,
        *,
        AccessToken: str,
        DeviceKey: str,
        DeviceSecretVerifierConfig: dict[str, Any] | None = None,
        DeviceName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def confirm_forgot_password(
        self,
        *,
        ClientId: str,
        Username: str,
        ConfirmationCode: str,
        Password: str,
        SecretHash: str | None = None,
        AnalyticsMetadata: dict[str, Any] | None = None,
        UserContextData: dict[str, Any] | None = None,
        ClientMetadata: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def confirm_sign_up(
        self,
        *,
        ClientId: str,
        Username: str,
        ConfirmationCode: str,
        SecretHash: str | None = None,
        ForceAliasCreation: bool | None = None,
        AnalyticsMetadata: dict[str, Any] | None = None,
        UserContextData: dict[str, Any] | None = None,
        ClientMetadata: dict[str, str] | None = None,
        Session: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cimd_policy(
        self,
        *,
        UserPoolId: str,
        ClientId: str,
        PolicyName: str,
        URLPatterns: list[str],
        CacheDuration: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_group(
        self,
        *,
        GroupName: str,
        UserPoolId: str,
        Description: str | None = None,
        RoleArn: str | None = None,
        Precedence: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_identity_provider(
        self,
        *,
        UserPoolId: str,
        ProviderName: str,
        ProviderType: str,
        ProviderDetails: dict[str, str],
        AttributeMapping: dict[str, str] | None = None,
        IdpIdentifiers: list[str] | None = None,
        AcrMapping: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_managed_login_branding(
        self,
        *,
        UserPoolId: str,
        ClientId: str,
        UseCognitoProvidedValues: bool | None = None,
        Settings: dict[str, Any] | None = None,
        Assets: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_resource_server(
        self,
        *,
        UserPoolId: str,
        Identifier: str,
        Name: str,
        Scopes: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_terms(
        self,
        *,
        UserPoolId: str,
        ClientId: str,
        TermsName: str,
        TermsSource: str,
        Enforcement: str,
        Links: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_user_import_job(
        self,
        *,
        JobName: str,
        UserPoolId: str,
        CloudWatchLogsRoleArn: str,
        PasswordHashingAlgorithm: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_user_pool(
        self,
        *,
        PoolName: str,
        Policies: dict[str, Any] | None = None,
        DeletionProtection: str | None = None,
        LambdaConfig: dict[str, Any] | None = None,
        AutoVerifiedAttributes: list[str] | None = None,
        AliasAttributes: list[str] | None = None,
        UsernameAttributes: list[str] | None = None,
        SmsVerificationMessage: str | None = None,
        EmailVerificationMessage: str | None = None,
        EmailVerificationSubject: str | None = None,
        VerificationMessageTemplate: dict[str, Any] | None = None,
        SmsAuthenticationMessage: str | None = None,
        MfaConfiguration: str | None = None,
        UserAttributeUpdateSettings: dict[str, Any] | None = None,
        DeviceConfiguration: dict[str, Any] | None = None,
        EmailConfiguration: dict[str, Any] | None = None,
        SmsConfiguration: dict[str, Any] | None = None,
        UserPoolTags: dict[str, str] | None = None,
        AdminCreateUserConfig: dict[str, Any] | None = None,
        Schema: list[dict[str, Any]] | None = None,
        UserPoolAddOns: dict[str, Any] | None = None,
        DcrConfiguration: dict[str, Any] | None = None,
        UsernameConfiguration: dict[str, Any] | None = None,
        AccountRecoverySetting: dict[str, Any] | None = None,
        UserPoolTier: str | None = None,
        KeyConfiguration: dict[str, Any] | None = None,
        IssuerConfiguration: dict[str, Any] | None = None,
        AcrConfiguration: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_user_pool_client(
        self,
        *,
        UserPoolId: str,
        ClientName: str,
        GenerateSecret: bool | None = None,
        ClientSecret: str | None = None,
        RefreshTokenValidity: int | None = None,
        AccessTokenValidity: int | None = None,
        IdTokenValidity: int | None = None,
        TokenValidityUnits: dict[str, Any] | None = None,
        ReadAttributes: list[str] | None = None,
        WriteAttributes: list[str] | None = None,
        ExplicitAuthFlows: list[str] | None = None,
        SupportedIdentityProviders: list[str] | None = None,
        CallbackURLs: list[str] | None = None,
        LogoutURLs: list[str] | None = None,
        DefaultRedirectURI: str | None = None,
        AllowedOAuthFlows: list[str] | None = None,
        AllowedOAuthScopes: list[str] | None = None,
        AllowedOAuthFlowsUserPoolClient: bool | None = None,
        AnalyticsConfiguration: dict[str, Any] | None = None,
        PreventUserExistenceErrors: str | None = None,
        EnableTokenRevocation: bool | None = None,
        EnablePropagateAdditionalUserContextData: bool | None = None,
        AuthSessionValidity: int | None = None,
        RefreshTokenRotation: dict[str, Any] | None = None,
        PublishSecretsInAWSSecretsManager: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_user_pool_domain(
        self,
        *,
        Domain: str,
        UserPoolId: str,
        ManagedLoginVersion: int | None = None,
        CustomDomainConfig: dict[str, Any] | None = None,
        Routing: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_user_pool_replica(
        self,
        *,
        UserPoolId: str,
        RegionName: str,
        UserPoolTags: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cimd_policy(
        self,
        *,
        UserPoolId: str,
        CIMDPolicyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_group(
        self,
        *,
        GroupName: str,
        UserPoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_identity_provider(
        self,
        *,
        UserPoolId: str,
        ProviderName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_managed_login_branding(
        self,
        *,
        ManagedLoginBrandingId: str,
        UserPoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_resource_server(
        self,
        *,
        UserPoolId: str,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_terms(
        self,
        *,
        TermsId: str,
        UserPoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user(
        self,
        *,
        AccessToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user_attributes(
        self,
        *,
        UserAttributeNames: list[str],
        AccessToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user_pool(
        self,
        *,
        UserPoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user_pool_client(
        self,
        *,
        UserPoolId: str,
        ClientId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user_pool_client_secret(
        self,
        *,
        UserPoolId: str,
        ClientId: str,
        ClientSecretId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user_pool_domain(
        self,
        *,
        Domain: str,
        UserPoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_user_pool_replica(
        self,
        *,
        UserPoolId: str,
        RegionName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_web_authn_credential(
        self,
        *,
        AccessToken: str,
        CredentialId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_cimd_policy(
        self,
        *,
        UserPoolId: str,
        CIMDPolicyId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_identity_provider(
        self,
        *,
        UserPoolId: str,
        ProviderName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_managed_login_branding(
        self,
        *,
        UserPoolId: str,
        ManagedLoginBrandingId: str,
        ReturnMergedResources: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_managed_login_branding_by_client(
        self,
        *,
        UserPoolId: str,
        ClientId: str,
        ReturnMergedResources: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_point_in_time_recovery(
        self,
        *,
        UserPoolId: str,
        RestoreId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_resource_server(
        self,
        *,
        UserPoolId: str,
        Identifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_risk_configuration(
        self,
        *,
        UserPoolId: str,
        ClientId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_terms(
        self,
        *,
        TermsId: str,
        UserPoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_terms_by_client(
        self,
        *,
        ClientId: str,
        UserPoolId: str,
        TermsName: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_user_import_job(
        self,
        *,
        UserPoolId: str,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_user_pool(
        self,
        *,
        UserPoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_user_pool_client(
        self,
        *,
        UserPoolId: str,
        ClientId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_user_pool_domain(
        self,
        *,
        Domain: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def forget_device(
        self,
        *,
        DeviceKey: str,
        AccessToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def forgot_password(
        self,
        *,
        ClientId: str,
        Username: str,
        SecretHash: str | None = None,
        UserContextData: dict[str, Any] | None = None,
        AnalyticsMetadata: dict[str, Any] | None = None,
        ClientMetadata: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_csv_header(
        self,
        *,
        UserPoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_client_token(
        self,
        *,
        ClientId: str,
        Secret: str,
        Scopes: list[str] | None = None,
        ClientMetadata: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_derived_token(
        self,
        *,
        ClientId: str,
        SubjectToken: str,
        SubjectTokenType: str,
        ClientSecret: str | None = None,
        SubjectTokenProviderName: str | None = None,
        ActorToken: str | None = None,
        ActorTokenType: str | None = None,
        ActorTokenProviderName: str | None = None,
        Scopes: list[str] | None = None,
        Audiences: list[str] | None = None,
        Resources: list[str] | None = None,
        RequestedTokenType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_device(
        self,
        *,
        DeviceKey: str,
        AccessToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_group(
        self,
        *,
        GroupName: str,
        UserPoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_identity_provider_by_identifier(
        self,
        *,
        UserPoolId: str,
        IdpIdentifier: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_log_delivery_configuration(
        self,
        *,
        UserPoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_provisioned_limit(
        self,
        *,
        LimitDefinition: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_signing_certificate(
        self,
        *,
        UserPoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_tokens_from_refresh_token(
        self,
        *,
        RefreshToken: str,
        ClientId: str,
        ClientSecret: str | None = None,
        DeviceKey: str | None = None,
        ClientMetadata: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_ui_customization(
        self,
        *,
        UserPoolId: str,
        ClientId: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_user(
        self,
        *,
        AccessToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_user_attribute_verification_code(
        self,
        *,
        AccessToken: str,
        AttributeName: str,
        ClientMetadata: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_user_auth_factors(
        self,
        *,
        AccessToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_user_pool_client_session_configuration(
        self,
        *,
        UserPoolId: str,
        ClientId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_user_pool_mfa_config(
        self,
        *,
        UserPoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_user_pool_session_configuration(
        self,
        *,
        UserPoolId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def global_sign_out(
        self,
        *,
        AccessToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def initiate_auth(
        self,
        *,
        AuthFlow: str,
        ClientId: str,
        AuthParameters: dict[str, str] | None = None,
        ClientMetadata: dict[str, str] | None = None,
        AnalyticsMetadata: dict[str, Any] | None = None,
        UserContextData: dict[str, Any] | None = None,
        Session: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def initiate_point_in_time_recovery(
        self,
        *,
        UserPoolId: str,
        RestoreTimestamp: datetime.datetime | str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_cimd_policies(
        self,
        *,
        UserPoolId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_client_metadata_urls(
        self,
        *,
        UserPoolId: str,
        CIMDPolicyId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_devices(
        self,
        *,
        AccessToken: str,
        Limit: int | None = None,
        PaginationToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_groups(
        self,
        *,
        UserPoolId: str,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_identity_providers(
        self,
        *,
        UserPoolId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_point_in_time_recoveries(
        self,
        *,
        UserPoolId: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_resource_servers(
        self,
        *,
        UserPoolId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        ResourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_terms(
        self,
        *,
        UserPoolId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_user_import_jobs(
        self,
        *,
        UserPoolId: str,
        MaxResults: int,
        PaginationToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_user_pool_client_secrets(
        self,
        *,
        UserPoolId: str,
        ClientId: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_user_pool_clients(
        self,
        *,
        UserPoolId: str,
        MaxResults: int | None = None,
        NextToken: str | None = None,
        ClientType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_user_pool_replicas(
        self,
        *,
        UserPoolId: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_user_pools(
        self,
        *,
        MaxResults: int,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_user_sessions(
        self,
        *,
        AccessToken: str,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_users(
        self,
        *,
        UserPoolId: str,
        AttributesToGet: list[str] | None = None,
        Limit: int | None = None,
        PaginationToken: str | None = None,
        Filter: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_users_in_group(
        self,
        *,
        UserPoolId: str,
        GroupName: str,
        Limit: int | None = None,
        NextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_web_authn_credentials(
        self,
        *,
        AccessToken: str,
        NextToken: str | None = None,
        MaxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def resend_confirmation_code(
        self,
        *,
        ClientId: str,
        Username: str,
        SecretHash: str | None = None,
        UserContextData: dict[str, Any] | None = None,
        AnalyticsMetadata: dict[str, Any] | None = None,
        ClientMetadata: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def respond_to_auth_challenge(
        self,
        *,
        ClientId: str,
        ChallengeName: str,
        Session: str | None = None,
        ChallengeResponses: dict[str, str] | None = None,
        AnalyticsMetadata: dict[str, Any] | None = None,
        UserContextData: dict[str, Any] | None = None,
        ClientMetadata: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def revoke_token(
        self,
        *,
        Token: str,
        ClientId: str,
        ClientSecret: str | None = None,
        RevokeAssociatedSessions: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def revoke_user_session(
        self,
        *,
        AccessToken: str,
        SessionId: str,
        RevokeAssociatedSessions: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_log_delivery_configuration(
        self,
        *,
        UserPoolId: str,
        LogConfigurations: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_risk_configuration(
        self,
        *,
        UserPoolId: str,
        ClientId: str | None = None,
        CompromisedCredentialsRiskConfiguration: dict[str, Any] | None = None,
        AccountTakeoverRiskConfiguration: dict[str, Any] | None = None,
        RiskExceptionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_ui_customization(
        self,
        *,
        UserPoolId: str,
        ClientId: str | None = None,
        CSS: str | None = None,
        ImageFile: bytes | BinaryIO | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_user_mfa_preference(
        self,
        *,
        AccessToken: str,
        SMSMfaSettings: dict[str, Any] | None = None,
        SoftwareTokenMfaSettings: dict[str, Any] | None = None,
        EmailMfaSettings: dict[str, Any] | None = None,
        WebAuthnMfaSettings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_user_pool_client_session_configuration(
        self,
        *,
        UserPoolId: str,
        ClientId: str,
        SSOSession: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_user_pool_mfa_config(
        self,
        *,
        UserPoolId: str,
        SmsMfaConfiguration: dict[str, Any] | None = None,
        SoftwareTokenMfaConfiguration: dict[str, Any] | None = None,
        EmailMfaConfiguration: dict[str, Any] | None = None,
        MfaConfiguration: str | None = None,
        WebAuthnConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_user_pool_session_configuration(
        self,
        *,
        UserPoolId: str,
        UserSessionTracking: str,
        TokenSession: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def set_user_settings(
        self,
        *,
        AccessToken: str,
        MFAOptions: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def sign_up(
        self,
        *,
        ClientId: str,
        Username: str,
        SecretHash: str | None = None,
        Password: str | None = None,
        UserAttributes: list[dict[str, Any]] | None = None,
        ValidationData: list[dict[str, Any]] | None = None,
        AnalyticsMetadata: dict[str, Any] | None = None,
        UserContextData: dict[str, Any] | None = None,
        ClientMetadata: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_point_in_time_recovery(
        self,
        *,
        UserPoolId: str,
        RestoreId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_user_import_job(
        self,
        *,
        UserPoolId: str,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_web_authn_registration(
        self,
        *,
        AccessToken: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_user_import_job(
        self,
        *,
        UserPoolId: str,
        JobId: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        ResourceArn: str,
        Tags: dict[str, str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        ResourceArn: str,
        TagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_auth_event_feedback(
        self,
        *,
        UserPoolId: str,
        Username: str,
        EventId: str,
        FeedbackToken: str,
        FeedbackValue: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_cimd_policy(
        self,
        *,
        UserPoolId: str,
        CIMDPolicyId: str,
        ClientId: str,
        URLPatterns: list[str],
        PolicyName: str | None = None,
        CacheDuration: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_client_metadata_url_state(
        self,
        *,
        UserPoolId: str,
        CIMDPolicyId: str,
        URL: str,
        Action: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_device_status(
        self,
        *,
        AccessToken: str,
        DeviceKey: str,
        DeviceRememberedStatus: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_group(
        self,
        *,
        GroupName: str,
        UserPoolId: str,
        Description: str | None = None,
        RoleArn: str | None = None,
        Precedence: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_identity_provider(
        self,
        *,
        UserPoolId: str,
        ProviderName: str,
        ProviderDetails: dict[str, str] | None = None,
        AttributeMapping: dict[str, str] | None = None,
        IdpIdentifiers: list[str] | None = None,
        AcrMapping: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_managed_login_branding(
        self,
        *,
        UserPoolId: str | None = None,
        ManagedLoginBrandingId: str | None = None,
        UseCognitoProvidedValues: bool | None = None,
        Settings: dict[str, Any] | None = None,
        Assets: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_provisioned_limit(
        self,
        *,
        LimitDefinition: dict[str, Any],
        RequestedLimitValue: int,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_resource_server(
        self,
        *,
        UserPoolId: str,
        Identifier: str,
        Name: str,
        Scopes: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_terms(
        self,
        *,
        TermsId: str,
        UserPoolId: str,
        TermsName: str | None = None,
        TermsSource: str | None = None,
        Enforcement: str | None = None,
        Links: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user_attributes(
        self,
        *,
        UserAttributes: list[dict[str, Any]],
        AccessToken: str,
        ClientMetadata: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user_pool(
        self,
        *,
        UserPoolId: str,
        Policies: dict[str, Any] | None = None,
        DeletionProtection: str | None = None,
        LambdaConfig: dict[str, Any] | None = None,
        AutoVerifiedAttributes: list[str] | None = None,
        SmsVerificationMessage: str | None = None,
        EmailVerificationMessage: str | None = None,
        EmailVerificationSubject: str | None = None,
        VerificationMessageTemplate: dict[str, Any] | None = None,
        SmsAuthenticationMessage: str | None = None,
        UserAttributeUpdateSettings: dict[str, Any] | None = None,
        MfaConfiguration: str | None = None,
        DeviceConfiguration: dict[str, Any] | None = None,
        EmailConfiguration: dict[str, Any] | None = None,
        SmsConfiguration: dict[str, Any] | None = None,
        UserPoolTags: dict[str, str] | None = None,
        AdminCreateUserConfig: dict[str, Any] | None = None,
        UserPoolAddOns: dict[str, Any] | None = None,
        DcrConfiguration: dict[str, Any] | None = None,
        AccountRecoverySetting: dict[str, Any] | None = None,
        PoolName: str | None = None,
        UserPoolTier: str | None = None,
        KeyConfiguration: dict[str, Any] | None = None,
        IssuerConfiguration: dict[str, Any] | None = None,
        AcrConfiguration: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user_pool_client(
        self,
        *,
        UserPoolId: str,
        ClientId: str,
        ClientName: str | None = None,
        RefreshTokenValidity: int | None = None,
        AccessTokenValidity: int | None = None,
        IdTokenValidity: int | None = None,
        TokenValidityUnits: dict[str, Any] | None = None,
        ReadAttributes: list[str] | None = None,
        WriteAttributes: list[str] | None = None,
        ExplicitAuthFlows: list[str] | None = None,
        SupportedIdentityProviders: list[str] | None = None,
        CallbackURLs: list[str] | None = None,
        LogoutURLs: list[str] | None = None,
        DefaultRedirectURI: str | None = None,
        AllowedOAuthFlows: list[str] | None = None,
        AllowedOAuthScopes: list[str] | None = None,
        AllowedOAuthFlowsUserPoolClient: bool | None = None,
        AnalyticsConfiguration: dict[str, Any] | None = None,
        PreventUserExistenceErrors: str | None = None,
        EnableTokenRevocation: bool | None = None,
        EnablePropagateAdditionalUserContextData: bool | None = None,
        AuthSessionValidity: int | None = None,
        RefreshTokenRotation: dict[str, Any] | None = None,
        PublishSecretsInAWSSecretsManager: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user_pool_domain(
        self,
        *,
        Domain: str,
        UserPoolId: str,
        ManagedLoginVersion: int | None = None,
        CustomDomainConfig: dict[str, Any] | None = None,
        Routing: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_user_pool_replica(
        self,
        *,
        UserPoolId: str,
        RegionName: str,
        Status: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def verify_software_token(
        self,
        *,
        UserCode: str,
        AccessToken: str | None = None,
        Session: str | None = None,
        FriendlyDeviceName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def verify_user_attribute(
        self,
        *,
        AccessToken: str,
        AttributeName: str,
        Code: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
