from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerRelationship(BaseModel):
    From: StrictStr | None = None
    To: StrictStr | None = None
