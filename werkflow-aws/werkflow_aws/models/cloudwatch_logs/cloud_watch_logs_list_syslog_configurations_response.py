from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_syslog_configuration import CloudWatchLogsSyslogConfiguration


class CloudWatchLogsListSyslogConfigurationsResponse(BaseModel):
    syslogConfigurations: list[CloudWatchLogsSyslogConfiguration] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
