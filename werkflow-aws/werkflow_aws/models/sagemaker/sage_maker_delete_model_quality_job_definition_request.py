from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteModelQualityJobDefinitionRequest(BaseModel):
    JobDefinitionName: StrictStr
