from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneWorkflowsMwaaPropertiesInput(BaseModel):
    mwaaEnvironmentName: StrictStr | None = None
