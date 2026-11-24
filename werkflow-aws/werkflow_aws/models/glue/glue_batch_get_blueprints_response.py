from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_blueprint import GlueBlueprint


class GlueBatchGetBlueprintsResponse(BaseModel):
    Blueprints: list[GlueBlueprint] | None = None
    MissingBlueprints: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
