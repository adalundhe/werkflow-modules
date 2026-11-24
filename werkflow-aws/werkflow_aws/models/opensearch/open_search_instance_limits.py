from __future__ import annotations
from pydantic import BaseModel
from .open_search_instance_count_limits import OpenSearchInstanceCountLimits


class OpenSearchInstanceLimits(BaseModel):
    InstanceCountLimits: OpenSearchInstanceCountLimits | None = None
