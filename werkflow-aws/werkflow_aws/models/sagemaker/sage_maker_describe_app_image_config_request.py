from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeAppImageConfigRequest(BaseModel):
    AppImageConfigName: StrictStr
