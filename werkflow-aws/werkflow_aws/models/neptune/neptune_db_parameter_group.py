from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneDBParameterGroup(BaseModel):
    DBParameterGroupName: StrictStr | None = None
    DBParameterGroupFamily: StrictStr | None = None
    Description: StrictStr | None = None
    DBParameterGroupArn: StrictStr | None = None
