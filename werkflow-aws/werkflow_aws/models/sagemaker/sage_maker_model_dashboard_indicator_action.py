from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SageMakerModelDashboardIndicatorAction(BaseModel):
    Enabled: StrictBool | None = None
