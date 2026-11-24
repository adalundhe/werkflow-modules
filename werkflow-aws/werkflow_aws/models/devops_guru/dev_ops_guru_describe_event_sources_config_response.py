from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dev_ops_guru_event_sources_config import DevOpsGuruEventSourcesConfig


class DevOpsGuruDescribeEventSourcesConfigResponse(BaseModel):
    EventSources: DevOpsGuruEventSourcesConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
