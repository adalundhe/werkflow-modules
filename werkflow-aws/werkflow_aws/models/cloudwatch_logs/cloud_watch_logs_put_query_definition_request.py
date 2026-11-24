from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_query_parameter import CloudWatchLogsQueryParameter


class CloudWatchLogsPutQueryDefinitionRequest(BaseModel):
    name: StrictStr
    queryString: StrictStr
    queryLanguage: Literal['CWLI', 'SQL', 'PPL'] | None = None
    queryDefinitionId: StrictStr | None = None
    logGroupNames: list[StrictStr] | None = None
    clientToken: StrictStr | None = None
    parameters: list[CloudWatchLogsQueryParameter] | None = None
