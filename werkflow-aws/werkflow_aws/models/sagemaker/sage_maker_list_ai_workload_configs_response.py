from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_ai_workload_config_summary import SageMakerAIWorkloadConfigSummary


class SageMakerListAIWorkloadConfigsResponse(BaseModel):
    AIWorkloadConfigs: list[SageMakerAIWorkloadConfigSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
