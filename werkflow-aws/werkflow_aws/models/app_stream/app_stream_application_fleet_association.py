from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamApplicationFleetAssociation(BaseModel):
    FleetName: StrictStr | None = None
    ApplicationArn: StrictStr | None = None
