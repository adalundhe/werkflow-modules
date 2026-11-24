from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBAvailabilityZone(BaseModel):
    Name: StrictStr | None = None
