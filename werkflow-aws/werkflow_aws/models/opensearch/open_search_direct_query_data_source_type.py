from __future__ import annotations
from pydantic import BaseModel
from .open_search_cloud_watch_direct_query_data_source import OpenSearchCloudWatchDirectQueryDataSource
from .open_search_prometheus_direct_query_data_source import OpenSearchPrometheusDirectQueryDataSource
from .open_search_security_lake_direct_query_data_source import OpenSearchSecurityLakeDirectQueryDataSource


class OpenSearchDirectQueryDataSourceType(BaseModel):
    CloudWatchLog: OpenSearchCloudWatchDirectQueryDataSource | None = None
    SecurityLake: OpenSearchSecurityLakeDirectQueryDataSource | None = None
    Prometheus: OpenSearchPrometheusDirectQueryDataSource | None = None
