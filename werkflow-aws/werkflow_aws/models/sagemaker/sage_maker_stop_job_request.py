from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SageMakerStopJobRequest(BaseModel):
    JobName: StrictStr
    JobCategory: Literal['AgentRFT', 'SyntheticDataGeneration', 'DataQualityEvaluation', 'AgentRFTEvaluation', 'DataTransformation']
