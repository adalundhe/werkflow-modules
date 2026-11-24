from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDescribeRecipeRequest(BaseModel):
    recipeArn: StrictStr
