from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .textract_blueprint_summary import TextractBlueprintSummary


class TextractListBlueprintsResponse(BaseModel):
    Blueprints: list[TextractBlueprintSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
