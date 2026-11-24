from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_configuration_template import CloudWatchLogsConfigurationTemplate


class CloudWatchLogsDescribeConfigurationTemplatesResponse(BaseModel):
    configurationTemplates: list[CloudWatchLogsConfigurationTemplate] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
