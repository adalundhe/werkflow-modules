from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMMaintenanceWindowStepFunctionsParameters(BaseModel):
    Input: StrictStr | None = None
    Name: StrictStr | None = None
