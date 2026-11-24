from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .cloud_watch_logs_data_source_filter import CloudWatchLogsDataSourceFilter
from .cloud_watch_logs_tag_filter import CloudWatchLogsTagFilter


class CloudWatchLogsListLogGroupsRequest(BaseModel):
    logGroupNamePattern: StrictStr | None = None
    logGroupClass: Literal['STANDARD', 'INFREQUENT_ACCESS', 'DELIVERY', 'ESSENTIALS'] | None = None
    includeLinkedAccounts: StrictBool | None = None
    accountIdentifiers: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
    limit: StrictInt | None = None
    dataSources: list[CloudWatchLogsDataSourceFilter] | None = None
    fieldIndexNames: list[StrictStr] | None = None
    logGroupTags: list[CloudWatchLogsTagFilter] | None = None
