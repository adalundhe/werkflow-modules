from __future__ import annotations
from pydantic import BaseModel
from .textract_blueprint_item import TextractBlueprintItem


class TextractCustomConfiguration(BaseModel):
    Blueprints: list[TextractBlueprintItem] | None = None
    FallbackBlueprints: list[TextractBlueprintItem] | None = None
