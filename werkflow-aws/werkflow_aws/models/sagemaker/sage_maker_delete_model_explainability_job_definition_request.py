from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteModelExplainabilityJobDefinitionRequest(BaseModel):
    JobDefinitionName: StrictStr
