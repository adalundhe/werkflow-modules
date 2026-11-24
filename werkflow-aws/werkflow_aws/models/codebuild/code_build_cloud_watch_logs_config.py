from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildCloudWatchLogsConfig(BaseModel):
    status: StrictStr | None = None
    groupName: StrictStr | None = None
    streamName: StrictStr | None = None
