from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_blueprint_run import GlueBlueprintRun


class GlueGetBlueprintRunsResponse(BaseModel):
    BlueprintRuns: list[GlueBlueprintRun] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
