from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_sync_cognito_config import AppSyncCognitoConfig
from .app_sync_lambda_authorizer_config import AppSyncLambdaAuthorizerConfig
from .app_sync_open_id_connect_config import AppSyncOpenIDConnectConfig


class AppSyncAuthProvider(BaseModel):
    authType: StrictStr | None = None
    cognitoConfig: AppSyncCognitoConfig | None = None
    openIDConnectConfig: AppSyncOpenIDConnectConfig | None = None
    lambdaAuthorizerConfig: AppSyncLambdaAuthorizerConfig | None = None
