from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_build_cloud_watch_logs_config import CodeBuildCloudWatchLogsConfig
from .code_build_s3_logs_config import CodeBuildS3LogsConfig


class CodeBuildLogsLocation(BaseModel):
    groupName: StrictStr | None = None
    streamName: StrictStr | None = None
    deepLink: StrictStr | None = None
    s3DeepLink: StrictStr | None = None
    cloudWatchLogsArn: StrictStr | None = None
    s3LogsArn: StrictStr | None = None
    cloudWatchLogs: CodeBuildCloudWatchLogsConfig | None = None
    s3Logs: CodeBuildS3LogsConfig | None = None
