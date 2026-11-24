from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerInstancePoolSummaryModel(BaseModel):
    InstanceType: StrictStr | None = None
    CurrentInstanceCount: StrictInt | None = None
