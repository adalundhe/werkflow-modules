from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class CloudWatchLogsDescribeLogGroupsRequest(BaseModel):
    accountIdentifiers: list[StrictStr] | None = None
    logGroupNamePrefix: StrictStr | None = None
    logGroupNamePattern: StrictStr | None = None
    nextToken: StrictStr | None = None
    limit: StrictInt | None = None
    includeLinkedAccounts: StrictBool | None = None
    logGroupClass: Literal['STANDARD', 'INFREQUENT_ACCESS', 'DELIVERY', 'ESSENTIALS'] | None = None
    logGroupIdentifiers: list[StrictStr] | None = None
