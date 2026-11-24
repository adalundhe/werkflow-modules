from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .app_sync_dynamodb_data_source_config import AppSyncDynamodbDataSourceConfig
from .app_sync_elasticsearch_data_source_config import AppSyncElasticsearchDataSourceConfig
from .app_sync_event_bridge_data_source_config import AppSyncEventBridgeDataSourceConfig
from .app_sync_http_data_source_config import AppSyncHttpDataSourceConfig
from .app_sync_lambda_data_source_config import AppSyncLambdaDataSourceConfig
from .app_sync_open_search_service_data_source_config import AppSyncOpenSearchServiceDataSourceConfig
from .app_sync_relational_database_data_source_config import AppSyncRelationalDatabaseDataSourceConfig


class AppSyncUpdateDataSourceRequest(BaseModel):
    apiId: StrictStr
    name: StrictStr
    type: Literal['AWS_LAMBDA', 'AMAZON_DYNAMODB', 'AMAZON_ELASTICSEARCH', 'NONE', 'HTTP', 'RELATIONAL_DATABASE', 'AMAZON_OPENSEARCH_SERVICE', 'AMAZON_EVENTBRIDGE', 'AMAZON_BEDROCK_RUNTIME']
    description: StrictStr | None = None
    serviceRoleArn: StrictStr | None = None
    dynamodbConfig: AppSyncDynamodbDataSourceConfig | None = None
    lambdaConfig: AppSyncLambdaDataSourceConfig | None = None
    elasticsearchConfig: AppSyncElasticsearchDataSourceConfig | None = None
    openSearchServiceConfig: AppSyncOpenSearchServiceDataSourceConfig | None = None
    httpConfig: AppSyncHttpDataSourceConfig | None = None
    relationalDatabaseConfig: AppSyncRelationalDatabaseDataSourceConfig | None = None
    eventBridgeConfig: AppSyncEventBridgeDataSourceConfig | None = None
    metricsConfig: Literal['ENABLED', 'DISABLED'] | None = None
