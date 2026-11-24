from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeDataQualityJobDefinitionRequest(BaseModel):
    JobDefinitionName: StrictStr
