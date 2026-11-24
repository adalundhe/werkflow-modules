from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeFieldsForThemeGeneration(BaseModel):
    itemName: StrictStr | None = None
