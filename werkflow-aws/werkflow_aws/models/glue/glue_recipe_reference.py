from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueRecipeReference(BaseModel):
    RecipeArn: StrictStr | None = None
    RecipeVersion: StrictStr | None = None
