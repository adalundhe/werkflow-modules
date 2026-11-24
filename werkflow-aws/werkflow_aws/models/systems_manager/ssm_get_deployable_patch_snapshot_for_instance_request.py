from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ssm_baseline_override import SSMBaselineOverride


class SSMGetDeployablePatchSnapshotForInstanceRequest(BaseModel):
    InstanceId: StrictStr
    SnapshotId: StrictStr
    BaselineOverride: SSMBaselineOverride | None = None
    UseS3DualStackEndpoint: StrictBool | None = None
