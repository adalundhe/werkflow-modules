from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSGatewayConnectorFilters(BaseModel):
    accessTypes: list[StrictStr] | None = None
