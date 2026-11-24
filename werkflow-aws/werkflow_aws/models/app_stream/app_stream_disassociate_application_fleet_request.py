from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamDisassociateApplicationFleetRequest(BaseModel):
    FleetName: StrictStr
    ApplicationArn: StrictStr
