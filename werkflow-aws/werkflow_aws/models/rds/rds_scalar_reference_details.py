from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class RDSScalarReferenceDetails(BaseModel):
    Value: StrictFloat | StrictInt | None = None
