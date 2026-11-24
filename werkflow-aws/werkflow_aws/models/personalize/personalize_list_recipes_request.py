from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class PersonalizeListRecipesRequest(BaseModel):
    recipeProvider: Literal['SERVICE'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    domain: Literal['ECOMMERCE', 'VIDEO_ON_DEMAND'] | None = None
