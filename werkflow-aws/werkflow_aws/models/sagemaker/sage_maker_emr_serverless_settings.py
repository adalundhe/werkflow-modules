from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerEmrServerlessSettings(BaseModel):
    ExecutionRoleArn: StrictStr | None = None
    Status: StrictStr | None = None
