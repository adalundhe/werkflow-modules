from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .personalize_recipe_summary import PersonalizeRecipeSummary


class PersonalizeListRecipesResponse(BaseModel):
    recipes: list[PersonalizeRecipeSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
