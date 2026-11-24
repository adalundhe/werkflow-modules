from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsCodeBuildProjectLogsConfigCloudWatchLogsDetails(BaseModel):
    GroupName: StrictStr | None = None
    Status: StrictStr | None = None
    StreamName: StrictStr | None = None
