from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .personalize_recipe import PersonalizeRecipe


class PersonalizeDescribeRecipeResponse(BaseModel):
    recipe: PersonalizeRecipe | None = None
    ResponseMetadata: dict[str, Any] | None = None
