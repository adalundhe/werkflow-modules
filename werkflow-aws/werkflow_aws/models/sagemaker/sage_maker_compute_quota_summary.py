from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_compute_quota_config import SageMakerComputeQuotaConfig
from .sage_maker_compute_quota_target import SageMakerComputeQuotaTarget


class SageMakerComputeQuotaSummary(BaseModel):
    ComputeQuotaArn: StrictStr | None = None
    ComputeQuotaId: StrictStr | None = None
    Name: StrictStr | None = None
    ComputeQuotaVersion: StrictInt | None = None
    Status: StrictStr | None = None
    ClusterArn: StrictStr | None = None
    ComputeQuotaConfig: SageMakerComputeQuotaConfig | None = None
    ComputeQuotaTarget: SageMakerComputeQuotaTarget | None = None
    ActivationState: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
