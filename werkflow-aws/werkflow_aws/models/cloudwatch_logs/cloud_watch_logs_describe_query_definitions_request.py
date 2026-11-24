from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsDescribeQueryDefinitionsRequest(BaseModel):
    queryLanguage: Literal['CWLI', 'SQL', 'PPL'] | None = None
    queryDefinitionNamePrefix: StrictStr | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
