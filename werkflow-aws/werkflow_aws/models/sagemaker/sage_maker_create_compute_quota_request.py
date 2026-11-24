from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .sage_maker_compute_quota_config import SageMakerComputeQuotaConfig
from .sage_maker_compute_quota_target import SageMakerComputeQuotaTarget
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateComputeQuotaRequest(BaseModel):
    Name: StrictStr
    ClusterArn: StrictStr
    ComputeQuotaConfig: SageMakerComputeQuotaConfig
    ComputeQuotaTarget: SageMakerComputeQuotaTarget
    Description: StrictStr | None = None
    ActivationState: Literal['Enabled', 'Disabled'] | None = None
    Tags: list[SageMakerTagModel] | None = None
