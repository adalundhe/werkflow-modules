from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeAutoMLResult(BaseModel):
    bestRecipeArn: StrictStr | None = None
