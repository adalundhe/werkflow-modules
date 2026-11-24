from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_sync_dynamodb_data_source_config import AppSyncDynamodbDataSourceConfig
from .app_sync_elasticsearch_data_source_config import AppSyncElasticsearchDataSourceConfig
from .app_sync_event_bridge_data_source_config import AppSyncEventBridgeDataSourceConfig
from .app_sync_http_data_source_config import AppSyncHttpDataSourceConfig
from .app_sync_lambda_data_source_config import AppSyncLambdaDataSourceConfig
from .app_sync_open_search_service_data_source_config import AppSyncOpenSearchServiceDataSourceConfig
from .app_sync_relational_database_data_source_config import AppSyncRelationalDatabaseDataSourceConfig


class AppSyncDataSource(BaseModel):
    dataSourceArn: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    type: StrictStr | None = None
    serviceRoleArn: StrictStr | None = None
    dynamodbConfig: AppSyncDynamodbDataSourceConfig | None = None
    lambdaConfig: AppSyncLambdaDataSourceConfig | None = None
    elasticsearchConfig: AppSyncElasticsearchDataSourceConfig | None = None
    openSearchServiceConfig: AppSyncOpenSearchServiceDataSourceConfig | None = None
    httpConfig: AppSyncHttpDataSourceConfig | None = None
    relationalDatabaseConfig: AppSyncRelationalDatabaseDataSourceConfig | None = None
    eventBridgeConfig: AppSyncEventBridgeDataSourceConfig | None = None
    metricsConfig: StrictStr | None = None
