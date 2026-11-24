from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueRecipeAction(BaseModel):
    Operation: StrictStr | None = None
    Parameters: dict[StrictStr, StrictStr] | None = None
