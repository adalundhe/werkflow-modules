from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_ai_dataset_config import SageMakerAIDatasetConfig
from .sage_maker_ai_workload_configs import SageMakerAIWorkloadConfigs
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateAIWorkloadConfigRequest(BaseModel):
    AIWorkloadConfigName: StrictStr
    DatasetConfig: SageMakerAIDatasetConfig | None = None
    AIWorkloadConfigs: SageMakerAIWorkloadConfigs | None = None
    Tags: list[SageMakerTagModel] | None = None
