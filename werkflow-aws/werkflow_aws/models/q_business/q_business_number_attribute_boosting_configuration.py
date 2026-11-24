from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessNumberAttributeBoostingConfiguration(BaseModel):
    boostingLevel: StrictStr | None = None
    boostingType: StrictStr | None = None
