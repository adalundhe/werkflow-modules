from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteDataQualityJobDefinitionRequest(BaseModel):
    JobDefinitionName: StrictStr
