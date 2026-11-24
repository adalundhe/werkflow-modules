from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_ai_workload_data_source import SageMakerAIWorkloadDataSource


class SageMakerAIWorkloadInputDataConfig(BaseModel):
    ChannelName: StrictStr | None = None
    DataSource: SageMakerAIWorkloadDataSource | None = None
