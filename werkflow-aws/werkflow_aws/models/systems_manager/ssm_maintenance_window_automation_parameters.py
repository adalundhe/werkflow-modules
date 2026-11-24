from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMMaintenanceWindowAutomationParameters(BaseModel):
    DocumentVersion: StrictStr | None = None
    Parameters: dict[StrictStr, list[StrictStr]] | None = None
