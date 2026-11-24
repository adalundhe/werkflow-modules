from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteModelBiasJobDefinitionRequest(BaseModel):
    JobDefinitionName: StrictStr
