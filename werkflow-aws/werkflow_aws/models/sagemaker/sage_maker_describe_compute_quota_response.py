from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_compute_quota_config import SageMakerComputeQuotaConfig
from .sage_maker_compute_quota_target import SageMakerComputeQuotaTarget
from .sage_maker_user_context_model import SageMakerUserContextModel


class SageMakerDescribeComputeQuotaResponse(BaseModel):
    ComputeQuotaArn: StrictStr | None = None
    ComputeQuotaId: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    ComputeQuotaVersion: StrictInt | None = None
    Status: StrictStr | None = None
    FailureReason: StrictStr | None = None
    ClusterArn: StrictStr | None = None
    ComputeQuotaConfig: SageMakerComputeQuotaConfig | None = None
    ComputeQuotaTarget: SageMakerComputeQuotaTarget | None = None
    ActivationState: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CreatedBy: SageMakerUserContextModel | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: SageMakerUserContextModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
