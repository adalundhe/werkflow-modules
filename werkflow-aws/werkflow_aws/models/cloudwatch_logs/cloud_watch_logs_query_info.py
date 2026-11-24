from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class CloudWatchLogsQueryInfo(BaseModel):
    queryLanguage: StrictStr | None = None
    queryId: StrictStr | None = None
    queryString: StrictStr | None = None
    status: StrictStr | None = None
    createTime: StrictInt | None = None
    logGroupName: StrictStr | None = None
    queryDuration: StrictInt | None = None
    bytesScanned: StrictFloat | StrictInt | None = None
    userIdentity: StrictStr | None = None
