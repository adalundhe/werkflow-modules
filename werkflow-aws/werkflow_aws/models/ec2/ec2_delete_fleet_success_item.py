from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2DeleteFleetSuccessItem(BaseModel):
    CurrentFleetState: StrictStr | None = None
    PreviousFleetState: StrictStr | None = None
    FleetId: StrictStr | None = None
