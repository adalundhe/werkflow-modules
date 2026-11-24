from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RDSLimitlessDatabaseModel(BaseModel):
    Status: StrictStr | None = None
    MinRequiredACU: StrictFloat | StrictInt | None = None
