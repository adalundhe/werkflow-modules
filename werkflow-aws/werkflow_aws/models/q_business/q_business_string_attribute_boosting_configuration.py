from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessStringAttributeBoostingConfiguration(BaseModel):
    boostingLevel: StrictStr | None = None
    attributeValueBoosting: dict[StrictStr, StrictStr] | None = None
