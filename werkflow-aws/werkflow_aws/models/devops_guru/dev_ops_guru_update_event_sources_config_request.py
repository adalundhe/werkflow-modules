from __future__ import annotations
from pydantic import BaseModel
from .dev_ops_guru_event_sources_config import DevOpsGuruEventSourcesConfig


class DevOpsGuruUpdateEventSourcesConfigRequest(BaseModel):
    EventSources: DevOpsGuruEventSourcesConfig | None = None
