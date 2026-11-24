from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamDisassociateFleetRequest(BaseModel):
    FleetName: StrictStr
    StackName: StrictStr
