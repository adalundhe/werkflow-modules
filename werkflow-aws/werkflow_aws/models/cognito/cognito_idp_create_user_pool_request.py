from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .cognito_idp_account_recovery_setting_type import CognitoIDPAccountRecoverySettingType
from .cognito_idp_acr_level_config_type import CognitoIDPAcrLevelConfigType
from .cognito_idp_admin_create_user_config_type import CognitoIDPAdminCreateUserConfigType
from .cognito_idp_dcr_configuration_type import CognitoIDPDcrConfigurationType
from .cognito_idp_device_configuration_type import CognitoIDPDeviceConfigurationType
from .cognito_idp_email_configuration_type import CognitoIDPEmailConfigurationType
from .cognito_idp_issuer_configuration_type import CognitoIDPIssuerConfigurationType
from .cognito_idp_key_configuration_type import CognitoIDPKeyConfigurationType
from .cognito_idp_lambda_config_type import CognitoIDPLambdaConfigType
from .cognito_idp_schema_attribute_type import CognitoIDPSchemaAttributeType
from .cognito_idp_sms_configuration_type import CognitoIDPSmsConfigurationType
from .cognito_idp_user_attribute_update_settings_type import CognitoIDPUserAttributeUpdateSettingsType
from .cognito_idp_user_pool_add_ons_type import CognitoIDPUserPoolAddOnsType
from .cognito_idp_user_pool_policy_type import CognitoIDPUserPoolPolicyType
from .cognito_idp_username_configuration_type import CognitoIDPUsernameConfigurationType
from .cognito_idp_verification_message_template_type import CognitoIDPVerificationMessageTemplateType


class CognitoIDPCreateUserPoolRequest(BaseModel):
    PoolName: StrictStr
    Policies: CognitoIDPUserPoolPolicyType | None = None
    DeletionProtection: Literal['ACTIVE', 'INACTIVE'] | None = None
    LambdaConfig: CognitoIDPLambdaConfigType | None = None
    AutoVerifiedAttributes: list[Literal['phone_number', 'email']] | None = None
    AliasAttributes: list[Literal['phone_number', 'email', 'preferred_username']] | None = None
    UsernameAttributes: list[Literal['phone_number', 'email']] | None = None
    SmsVerificationMessage: StrictStr | None = None
    EmailVerificationMessage: StrictStr | None = None
    EmailVerificationSubject: StrictStr | None = None
    VerificationMessageTemplate: CognitoIDPVerificationMessageTemplateType | None = None
    SmsAuthenticationMessage: StrictStr | None = None
    MfaConfiguration: Literal['OFF', 'ON', 'OPTIONAL'] | None = None
    UserAttributeUpdateSettings: CognitoIDPUserAttributeUpdateSettingsType | None = None
    DeviceConfiguration: CognitoIDPDeviceConfigurationType | None = None
    EmailConfiguration: CognitoIDPEmailConfigurationType | None = None
    SmsConfiguration: CognitoIDPSmsConfigurationType | None = None
    UserPoolTags: dict[StrictStr, StrictStr] | None = None
    AdminCreateUserConfig: CognitoIDPAdminCreateUserConfigType | None = None
    Schema: list[CognitoIDPSchemaAttributeType] | None = None
    UserPoolAddOns: CognitoIDPUserPoolAddOnsType | None = None
    DcrConfiguration: CognitoIDPDcrConfigurationType | None = None
    UsernameConfiguration: CognitoIDPUsernameConfigurationType | None = None
    AccountRecoverySetting: CognitoIDPAccountRecoverySettingType | None = None
    UserPoolTier: Literal['LITE', 'ESSENTIALS', 'PLUS'] | None = None
    KeyConfiguration: CognitoIDPKeyConfigurationType | None = None
    IssuerConfiguration: CognitoIDPIssuerConfigurationType | None = None
    AcrConfiguration: dict[StrictStr, CognitoIDPAcrLevelConfigType] | None = None
