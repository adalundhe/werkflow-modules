from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamAssociateFleetRequest(BaseModel):
    FleetName: StrictStr
    StackName: StrictStr
