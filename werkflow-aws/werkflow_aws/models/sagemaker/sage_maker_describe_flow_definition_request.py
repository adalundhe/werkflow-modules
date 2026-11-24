from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeFlowDefinitionRequest(BaseModel):
    FlowDefinitionName: StrictStr
