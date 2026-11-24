from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_recipe_reference import GlueRecipeReference
from .glue_recipe_step import GlueRecipeStep


class GlueRecipe(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    RecipeReference: GlueRecipeReference | None = None
    RecipeSteps: list[GlueRecipeStep] | None = None
