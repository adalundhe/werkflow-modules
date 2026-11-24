from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeAutoMLConfig(BaseModel):
    metricName: StrictStr | None = None
    recipeList: list[StrictStr] | None = None
