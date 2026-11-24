from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_ai_workload_input_data_config import SageMakerAIWorkloadInputDataConfig


class SageMakerAIDatasetConfig(BaseModel):
    InputDataConfig: list[SageMakerAIWorkloadInputDataConfig] | None = None
