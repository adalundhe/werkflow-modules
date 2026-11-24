from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_blueprint import LightsailBlueprint


class LightsailGetBlueprintsResponse(BaseModel):
    blueprints: list[LightsailBlueprint] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
