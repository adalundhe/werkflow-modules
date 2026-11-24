from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDeleteApplicationRequest(BaseModel):
    id: StrictStr
