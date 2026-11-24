from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_logs_open_search_application import CloudWatchLogsOpenSearchApplication
from .cloud_watch_logs_open_search_collection import CloudWatchLogsOpenSearchCollection
from .cloud_watch_logs_open_search_data_access_policy import CloudWatchLogsOpenSearchDataAccessPolicy
from .cloud_watch_logs_open_search_data_source import CloudWatchLogsOpenSearchDataSource
from .cloud_watch_logs_open_search_encryption_policy import CloudWatchLogsOpenSearchEncryptionPolicy
from .cloud_watch_logs_open_search_lifecycle_policy import CloudWatchLogsOpenSearchLifecyclePolicy
from .cloud_watch_logs_open_search_network_policy import CloudWatchLogsOpenSearchNetworkPolicy
from .cloud_watch_logs_open_search_workspace import CloudWatchLogsOpenSearchWorkspace


class CloudWatchLogsOpenSearchIntegrationDetails(BaseModel):
    dataSource: CloudWatchLogsOpenSearchDataSource | None = None
    application: CloudWatchLogsOpenSearchApplication | None = None
    collection: CloudWatchLogsOpenSearchCollection | None = None
    workspace: CloudWatchLogsOpenSearchWorkspace | None = None
    encryptionPolicy: CloudWatchLogsOpenSearchEncryptionPolicy | None = None
    networkPolicy: CloudWatchLogsOpenSearchNetworkPolicy | None = None
    accessPolicy: CloudWatchLogsOpenSearchDataAccessPolicy | None = None
    lifecyclePolicy: CloudWatchLogsOpenSearchLifecyclePolicy | None = None
