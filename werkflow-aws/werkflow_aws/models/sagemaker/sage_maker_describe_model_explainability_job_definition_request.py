from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeModelExplainabilityJobDefinitionRequest(BaseModel):
    JobDefinitionName: StrictStr
