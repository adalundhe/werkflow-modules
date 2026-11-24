from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3ReplicaModifications(BaseModel):
    Status: StrictStr | None = None
