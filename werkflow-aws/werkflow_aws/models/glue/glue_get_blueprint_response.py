from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_blueprint import GlueBlueprint


class GlueGetBlueprintResponse(BaseModel):
    Blueprint: GlueBlueprint | None = None
    ResponseMetadata: dict[str, Any] | None = None
