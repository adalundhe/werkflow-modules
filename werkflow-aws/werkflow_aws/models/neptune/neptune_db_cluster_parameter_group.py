from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneDBClusterParameterGroup(BaseModel):
    DBClusterParameterGroupName: StrictStr | None = None
    DBParameterGroupFamily: StrictStr | None = None
    Description: StrictStr | None = None
    DBClusterParameterGroupArn: StrictStr | None = None
