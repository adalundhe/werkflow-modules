from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDBParameterGroupStatus(BaseModel):
    DBParameterGroupName: StrictStr | None = None
    ParameterApplyStatus: StrictStr | None = None
