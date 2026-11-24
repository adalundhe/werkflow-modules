from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_aws_app_sync_graph_ql_api_additional_authentication_providers_details import SecurityHubAwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails
from .security_hub_aws_app_sync_graph_ql_api_lambda_authorizer_config_details import SecurityHubAwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails
from .security_hub_aws_app_sync_graph_ql_api_log_config_details import SecurityHubAwsAppSyncGraphQlApiLogConfigDetails
from .security_hub_aws_app_sync_graph_ql_api_open_id_connect_config_details import SecurityHubAwsAppSyncGraphQlApiOpenIdConnectConfigDetails
from .security_hub_aws_app_sync_graph_ql_api_user_pool_config_details import SecurityHubAwsAppSyncGraphQlApiUserPoolConfigDetails


class SecurityHubAwsAppSyncGraphQlApiDetails(BaseModel):
    ApiId: StrictStr | None = None
    Id: StrictStr | None = None
    OpenIdConnectConfig: SecurityHubAwsAppSyncGraphQlApiOpenIdConnectConfigDetails | None = None
    Name: StrictStr | None = None
    LambdaAuthorizerConfig: SecurityHubAwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails | None = None
    XrayEnabled: StrictBool | None = None
    Arn: StrictStr | None = None
    UserPoolConfig: SecurityHubAwsAppSyncGraphQlApiUserPoolConfigDetails | None = None
    AuthenticationType: StrictStr | None = None
    LogConfig: SecurityHubAwsAppSyncGraphQlApiLogConfigDetails | None = None
    AdditionalAuthenticationProviders: list[SecurityHubAwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails] | None = None
    WafWebAclArn: StrictStr | None = None
