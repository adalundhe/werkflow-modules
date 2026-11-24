from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QBusinessDateAttributeBoostingConfiguration(BaseModel):
    boostingLevel: StrictStr | None = None
    boostingDurationInSeconds: StrictInt | None = None
