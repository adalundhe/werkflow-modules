from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamAssociateApplicationFleetRequest(BaseModel):
    FleetName: StrictStr
    ApplicationArn: StrictStr
