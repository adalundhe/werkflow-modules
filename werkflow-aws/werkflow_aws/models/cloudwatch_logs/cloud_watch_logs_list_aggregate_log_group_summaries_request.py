from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cloud_watch_logs_data_source_filter import CloudWatchLogsDataSourceFilter


class CloudWatchLogsListAggregateLogGroupSummariesRequest(BaseModel):
    groupBy: Literal['DATA_SOURCE_NAME_TYPE_AND_FORMAT', 'DATA_SOURCE_NAME_AND_TYPE']
    accountIdentifiers: list[StrictStr] | None = None
    includeLinkedAccounts: StrictBool | None = None
    logGroupClass: Literal['STANDARD', 'INFREQUENT_ACCESS', 'DELIVERY', 'ESSENTIALS'] | None = None
    logGroupNamePattern: StrictStr | None = None
    dataSources: list[CloudWatchLogsDataSourceFilter] | None = None
    nextToken: StrictStr | None = None
    limit: StrictInt | None = None
