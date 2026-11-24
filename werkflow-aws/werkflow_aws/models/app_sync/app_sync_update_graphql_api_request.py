from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .app_sync_additional_authentication_provider import AppSyncAdditionalAuthenticationProvider
from .app_sync_enhanced_metrics_config import AppSyncEnhancedMetricsConfig
from .app_sync_lambda_authorizer_config import AppSyncLambdaAuthorizerConfig
from .app_sync_log_config import AppSyncLogConfig
from .app_sync_open_id_connect_config import AppSyncOpenIDConnectConfig
from .app_sync_user_pool_config import AppSyncUserPoolConfig


class AppSyncUpdateGraphqlApiRequest(BaseModel):
    apiId: StrictStr
    name: StrictStr
    authenticationType: Literal['API_KEY', 'AWS_IAM', 'AMAZON_COGNITO_USER_POOLS', 'OPENID_CONNECT', 'AWS_LAMBDA']
    logConfig: AppSyncLogConfig | None = None
    userPoolConfig: AppSyncUserPoolConfig | None = None
    openIDConnectConfig: AppSyncOpenIDConnectConfig | None = None
    additionalAuthenticationProviders: list[AppSyncAdditionalAuthenticationProvider] | None = None
    xrayEnabled: StrictBool | None = None
    lambdaAuthorizerConfig: AppSyncLambdaAuthorizerConfig | None = None
    mergedApiExecutionRoleArn: StrictStr | None = None
    ownerContact: StrictStr | None = None
    introspectionConfig: Literal['ENABLED', 'DISABLED'] | None = None
    queryDepthLimit: StrictInt | None = None
    resolverCountLimit: StrictInt | None = None
    enhancedMetricsConfig: AppSyncEnhancedMetricsConfig | None = None
