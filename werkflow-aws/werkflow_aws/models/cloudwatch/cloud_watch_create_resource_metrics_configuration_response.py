from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_watch_resource_metrics_configuration import CloudWatchResourceMetricsConfiguration


class CloudWatchCreateResourceMetricsConfigurationResponse(BaseModel):
    ResourceMetricsConfiguration: CloudWatchResourceMetricsConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
