from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerClusterInstanceRequirementDetails(BaseModel):
    CurrentInstanceTypes: list[StrictStr] | None = None
    DesiredInstanceTypes: list[StrictStr] | None = None
