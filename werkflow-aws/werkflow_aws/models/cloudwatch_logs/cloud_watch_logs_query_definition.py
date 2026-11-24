from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .cloud_watch_logs_query_parameter import CloudWatchLogsQueryParameter


class CloudWatchLogsQueryDefinition(BaseModel):
    queryLanguage: StrictStr | None = None
    queryDefinitionId: StrictStr | None = None
    name: StrictStr | None = None
    queryString: StrictStr | None = None
    lastModified: StrictInt | None = None
    logGroupNames: list[StrictStr] | None = None
    parameters: list[CloudWatchLogsQueryParameter] | None = None
