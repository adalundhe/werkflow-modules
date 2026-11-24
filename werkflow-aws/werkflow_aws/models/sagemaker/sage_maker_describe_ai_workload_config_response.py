from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_ai_dataset_config import SageMakerAIDatasetConfig
from .sage_maker_ai_workload_configs import SageMakerAIWorkloadConfigs
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerDescribeAIWorkloadConfigResponse(BaseModel):
    AIWorkloadConfigName: StrictStr | None = None
    AIWorkloadConfigArn: StrictStr | None = None
    DatasetConfig: SageMakerAIDatasetConfig | None = None
    AIWorkloadConfigs: SageMakerAIWorkloadConfigs | None = None
    Tags: list[SageMakerTagModel] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
