from __future__ import annotations
from pydantic import BaseModel
from .code_build_cloud_watch_logs_config import CodeBuildCloudWatchLogsConfig
from .code_build_s3_logs_config import CodeBuildS3LogsConfig


class CodeBuildLogsConfig(BaseModel):
    cloudWatchLogs: CodeBuildCloudWatchLogsConfig | None = None
    s3Logs: CodeBuildS3LogsConfig | None = None
