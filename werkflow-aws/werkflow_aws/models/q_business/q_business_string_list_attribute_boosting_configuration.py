from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessStringListAttributeBoostingConfiguration(BaseModel):
    boostingLevel: StrictStr | None = None
