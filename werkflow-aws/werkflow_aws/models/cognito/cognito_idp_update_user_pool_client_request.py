from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cognito_idp_analytics_configuration_type import CognitoIDPAnalyticsConfigurationType
from .cognito_idp_refresh_token_rotation_type import CognitoIDPRefreshTokenRotationType
from .cognito_idp_token_validity_units_type import CognitoIDPTokenValidityUnitsType


class CognitoIDPUpdateUserPoolClientRequest(BaseModel):
    UserPoolId: StrictStr
    ClientId: StrictStr
    ClientName: StrictStr | None = None
    RefreshTokenValidity: StrictInt | None = None
    AccessTokenValidity: StrictInt | None = None
    IdTokenValidity: StrictInt | None = None
    TokenValidityUnits: CognitoIDPTokenValidityUnitsType | None = None
    ReadAttributes: list[StrictStr] | None = None
    WriteAttributes: list[StrictStr] | None = None
    ExplicitAuthFlows: list[Literal['ADMIN_NO_SRP_AUTH', 'CUSTOM_AUTH_FLOW_ONLY', 'USER_PASSWORD_AUTH', 'ALLOW_ADMIN_USER_PASSWORD_AUTH', 'ALLOW_CUSTOM_AUTH', 'ALLOW_USER_PASSWORD_AUTH', 'ALLOW_USER_SRP_AUTH', 'ALLOW_REFRESH_TOKEN_AUTH', 'ALLOW_USER_AUTH', 'ALLOW_TOKEN_EXCHANGE_DELEGATION', 'ALLOW_TOKEN_EXCHANGE_IMPERSONATION']] | None = None
    SupportedIdentityProviders: list[StrictStr] | None = None
    CallbackURLs: list[StrictStr] | None = None
    LogoutURLs: list[StrictStr] | None = None
    DefaultRedirectURI: StrictStr | None = None
    AllowedOAuthFlows: list[Literal['code', 'implicit', 'client_credentials']] | None = None
    AllowedOAuthScopes: list[StrictStr] | None = None
    AllowedOAuthFlowsUserPoolClient: StrictBool | None = None
    AnalyticsConfiguration: CognitoIDPAnalyticsConfigurationType | None = None
    PreventUserExistenceErrors: Literal['LEGACY', 'ENABLED'] | None = None
    EnableTokenRevocation: StrictBool | None = None
    EnablePropagateAdditionalUserContextData: StrictBool | None = None
    AuthSessionValidity: StrictInt | None = None
    RefreshTokenRotation: CognitoIDPRefreshTokenRotationType | None = None
    PublishSecretsInAWSSecretsManager: StrictBool | None = None
