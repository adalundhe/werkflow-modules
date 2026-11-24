from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3DeleteMarkerReplication(BaseModel):
    Status: StrictStr | None = None
