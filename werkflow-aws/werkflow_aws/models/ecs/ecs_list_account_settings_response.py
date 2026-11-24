from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecs_setting import ECSSetting


class ECSListAccountSettingsResponse(BaseModel):
    settings: list[ECSSetting] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
