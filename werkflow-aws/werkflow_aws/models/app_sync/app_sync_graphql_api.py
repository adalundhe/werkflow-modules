from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .app_sync_additional_authentication_provider import AppSyncAdditionalAuthenticationProvider
from .app_sync_enhanced_metrics_config import AppSyncEnhancedMetricsConfig
from .app_sync_lambda_authorizer_config import AppSyncLambdaAuthorizerConfig
from .app_sync_log_config import AppSyncLogConfig
from .app_sync_open_id_connect_config import AppSyncOpenIDConnectConfig
from .app_sync_user_pool_config import AppSyncUserPoolConfig


class AppSyncGraphqlApi(BaseModel):
    name: StrictStr | None = None
    apiId: StrictStr | None = None
    authenticationType: StrictStr | None = None
    logConfig: AppSyncLogConfig | None = None
    userPoolConfig: AppSyncUserPoolConfig | None = None
    openIDConnectConfig: AppSyncOpenIDConnectConfig | None = None
    arn: StrictStr | None = None
    uris: dict[StrictStr, StrictStr] | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    additionalAuthenticationProviders: list[AppSyncAdditionalAuthenticationProvider] | None = None
    xrayEnabled: StrictBool | None = None
    wafWebAclArn: StrictStr | None = None
    lambdaAuthorizerConfig: AppSyncLambdaAuthorizerConfig | None = None
    dns: dict[StrictStr, StrictStr] | None = None
    visibility: StrictStr | None = None
    apiType: StrictStr | None = None
    mergedApiExecutionRoleArn: StrictStr | None = None
    owner: StrictStr | None = None
    ownerContact: StrictStr | None = None
    introspectionConfig: StrictStr | None = None
    queryDepthLimit: StrictInt | None = None
    resolverCountLimit: StrictInt | None = None
    enhancedMetricsConfig: AppSyncEnhancedMetricsConfig | None = None
