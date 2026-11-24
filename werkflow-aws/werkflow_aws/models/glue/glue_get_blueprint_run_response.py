from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_blueprint_run import GlueBlueprintRun


class GlueGetBlueprintRunResponse(BaseModel):
    BlueprintRun: GlueBlueprintRun | None = None
    ResponseMetadata: dict[str, Any] | None = None
