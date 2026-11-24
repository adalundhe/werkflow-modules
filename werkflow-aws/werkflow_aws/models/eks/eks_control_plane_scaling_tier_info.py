from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .eks_control_plane_config_info import EKSControlPlaneConfigInfo


class EKSControlPlaneScalingTierInfo(BaseModel):
    tierName: StrictStr | None = None
    apiRequestConcurrency: StrictInt | None = None
    podSchedulingRatePerSecond: StrictInt | None = None
    clusterDatabaseSizeGb: StrictInt | None = None
    controlPlaneComponentConfigOverrides: EKSControlPlaneConfigInfo | None = None
