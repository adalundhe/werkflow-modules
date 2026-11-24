from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneWorkflowsMwaaPropertiesOutput(BaseModel):
    mwaaEnvironmentName: StrictStr | None = None
