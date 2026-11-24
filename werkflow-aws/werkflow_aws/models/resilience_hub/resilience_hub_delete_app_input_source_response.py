from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_app_input_source import ResilienceHubAppInputSource


class ResilienceHubDeleteAppInputSourceResponse(BaseModel):
    appArn: StrictStr | None = None
    appInputSource: ResilienceHubAppInputSource | None = None
    ResponseMetadata: dict[str, Any] | None = None
