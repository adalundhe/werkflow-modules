from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDescribeFieldIndexesRequest(BaseModel):
    logGroupIdentifiers: list[StrictStr]
    indexCategories: list[Literal['DEFAULT', 'CUSTOM', 'AUTO', 'INACTIVE']] | None = None
    nextToken: StrictStr | None = None
