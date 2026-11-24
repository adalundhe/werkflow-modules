from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsListLogAnomalyDetectorsRequest(BaseModel):
    filterLogGroupArn: StrictStr | None = None
    limit: StrictInt | None = None
    nextToken: StrictStr | None = None
