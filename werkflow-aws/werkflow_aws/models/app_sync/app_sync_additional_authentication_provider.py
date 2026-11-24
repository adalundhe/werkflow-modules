from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_sync_cognito_user_pool_config import AppSyncCognitoUserPoolConfig
from .app_sync_lambda_authorizer_config import AppSyncLambdaAuthorizerConfig
from .app_sync_open_id_connect_config import AppSyncOpenIDConnectConfig


class AppSyncAdditionalAuthenticationProvider(BaseModel):
    authenticationType: StrictStr | None = None
    openIDConnectConfig: AppSyncOpenIDConnectConfig | None = None
    userPoolConfig: AppSyncCognitoUserPoolConfig | None = None
    lambdaAuthorizerConfig: AppSyncLambdaAuthorizerConfig | None = None
