from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_compute_quota_resource_config import SageMakerComputeQuotaResourceConfig
from .sage_maker_resource_sharing_config import SageMakerResourceSharingConfig


class SageMakerComputeQuotaConfig(BaseModel):
    ComputeQuotaResources: list[SageMakerComputeQuotaResourceConfig] | None = None
    ResourceSharingConfig: SageMakerResourceSharingConfig | None = None
    PreemptTeamTasks: StrictStr | None = None
