from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .eks_control_plane_config_info import EKSControlPlaneConfigInfo
from .eks_control_plane_scaling_tier_info import EKSControlPlaneScalingTierInfo


class EKSClusterVersionInformation(BaseModel):
    clusterVersion: StrictStr | None = None
    clusterType: StrictStr | None = None
    defaultPlatformVersion: StrictStr | None = None
    defaultVersion: StrictBool | None = None
    releaseDate: datetime.datetime | StrictStr | None = None
    endOfStandardSupportDate: datetime.datetime | StrictStr | None = None
    endOfExtendedSupportDate: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    versionStatus: StrictStr | None = None
    kubernetesPatchVersion: StrictStr | None = None
    controlPlaneScalingTiers: list[EKSControlPlaneScalingTierInfo] | None = None
    controlPlaneComponentConfig: EKSControlPlaneConfigInfo | None = None
