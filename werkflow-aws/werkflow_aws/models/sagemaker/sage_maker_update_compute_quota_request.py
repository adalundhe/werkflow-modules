from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_compute_quota_config import SageMakerComputeQuotaConfig
from .sage_maker_compute_quota_target import SageMakerComputeQuotaTarget


class SageMakerUpdateComputeQuotaRequest(BaseModel):
    ComputeQuotaId: StrictStr
    TargetVersion: StrictInt
    ComputeQuotaConfig: SageMakerComputeQuotaConfig | None = None
    ComputeQuotaTarget: SageMakerComputeQuotaTarget | None = None
    ActivationState: Literal['Enabled', 'Disabled'] | None = None
    Description: StrictStr | None = None
