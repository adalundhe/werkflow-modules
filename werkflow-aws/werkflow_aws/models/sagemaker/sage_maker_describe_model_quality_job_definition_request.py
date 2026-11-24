from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeModelQualityJobDefinitionRequest(BaseModel):
    JobDefinitionName: StrictStr
