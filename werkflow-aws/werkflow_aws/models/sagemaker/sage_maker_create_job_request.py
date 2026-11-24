from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateJobRequest(BaseModel):
    JobName: StrictStr
    RoleArn: StrictStr
    JobCategory: Literal['AgentRFT', 'SyntheticDataGeneration', 'DataQualityEvaluation', 'AgentRFTEvaluation', 'DataTransformation']
    JobConfigSchemaVersion: StrictStr
    JobConfigDocument: StrictStr
    Tags: list[SageMakerTagModel] | None = None
