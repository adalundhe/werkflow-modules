from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .resilience_hub_app import ResilienceHubApp


class ResilienceHubCreateAppResponse(BaseModel):
    app: ResilienceHubApp | None = None
    ResponseMetadata: dict[str, Any] | None = None
