from __future__ import annotations
from pydantic import BaseModel
from .open_search_serverless_capacity_limits import OpenSearchServerlessCapacityLimits


class OpenSearchServerlessUpdateAccountSettingsRequest(BaseModel):
    capacityLimits: OpenSearchServerlessCapacityLimits | None = None
