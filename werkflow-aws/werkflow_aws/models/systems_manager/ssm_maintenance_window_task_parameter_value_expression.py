from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMMaintenanceWindowTaskParameterValueExpression(BaseModel):
    Values: list[StrictStr] | None = None
