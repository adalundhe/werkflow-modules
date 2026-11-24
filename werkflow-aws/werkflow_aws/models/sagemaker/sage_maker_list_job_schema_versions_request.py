from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListJobSchemaVersionsRequest(BaseModel):
    JobCategory: Literal['AgentRFT', 'SyntheticDataGeneration', 'DataQualityEvaluation', 'AgentRFTEvaluation', 'DataTransformation']
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
