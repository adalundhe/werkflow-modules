from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cognito_idp_analytics_configuration_type import CognitoIDPAnalyticsConfigurationType
from .cognito_idp_refresh_token_rotation_type import CognitoIDPRefreshTokenRotationType
from .cognito_idp_token_validity_units_type import CognitoIDPTokenValidityUnitsType


class CognitoIDPUserPoolClientType(BaseModel):
    UserPoolId: StrictStr | None = None
    ClientName: StrictStr | None = None
    ClientId: StrictStr | None = None
    ClientSecret: StrictStr | None = None
    ClientSecretArn: StrictStr | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    RefreshTokenValidity: StrictInt | None = None
    AccessTokenValidity: StrictInt | None = None
    IdTokenValidity: StrictInt | None = None
    TokenValidityUnits: CognitoIDPTokenValidityUnitsType | None = None
    ReadAttributes: list[StrictStr] | None = None
    WriteAttributes: list[StrictStr] | None = None
    ExplicitAuthFlows: list[StrictStr] | None = None
    SupportedIdentityProviders: list[StrictStr] | None = None
    CallbackURLs: list[StrictStr] | None = None
    LogoutURLs: list[StrictStr] | None = None
    DefaultRedirectURI: StrictStr | None = None
    AllowedOAuthFlows: list[StrictStr] | None = None
    AllowedOAuthScopes: list[StrictStr] | None = None
    AllowedOAuthFlowsUserPoolClient: StrictBool | None = None
    AnalyticsConfiguration: CognitoIDPAnalyticsConfigurationType | None = None
    PreventUserExistenceErrors: StrictStr | None = None
    EnableTokenRevocation: StrictBool | None = None
    EnablePropagateAdditionalUserContextData: StrictBool | None = None
    AuthSessionValidity: StrictInt | None = None
    RefreshTokenRotation: CognitoIDPRefreshTokenRotationType | None = None
    ClientType: StrictStr | None = None
