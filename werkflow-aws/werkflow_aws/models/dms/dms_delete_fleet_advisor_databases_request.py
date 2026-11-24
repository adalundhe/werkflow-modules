from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSDeleteFleetAdvisorDatabasesRequest(BaseModel):
    DatabaseIds: list[StrictStr]
