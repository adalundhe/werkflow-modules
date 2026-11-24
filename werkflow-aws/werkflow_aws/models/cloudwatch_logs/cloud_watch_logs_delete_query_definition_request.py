from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsDeleteQueryDefinitionRequest(BaseModel):
    queryDefinitionId: StrictStr
