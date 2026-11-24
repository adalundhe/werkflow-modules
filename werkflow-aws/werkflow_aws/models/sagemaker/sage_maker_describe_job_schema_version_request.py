from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SageMakerDescribeJobSchemaVersionRequest(BaseModel):
    JobCategory: Literal['AgentRFT', 'SyntheticDataGeneration', 'DataQualityEvaluation', 'AgentRFTEvaluation', 'DataTransformation']
    JobConfigSchemaVersion: StrictStr | None = None
