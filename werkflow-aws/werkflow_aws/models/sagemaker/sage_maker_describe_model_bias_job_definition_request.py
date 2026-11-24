from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeModelBiasJobDefinitionRequest(BaseModel):
    JobDefinitionName: StrictStr
