from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchSavedObjectIdentifier(BaseModel):
    type: StrictStr
    id: StrictStr
