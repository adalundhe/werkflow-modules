from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSCustomDBEngineVersionAMI(BaseModel):
    ImageId: StrictStr | None = None
    Status: StrictStr | None = None
