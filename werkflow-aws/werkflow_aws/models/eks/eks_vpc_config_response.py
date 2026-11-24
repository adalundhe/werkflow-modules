from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .eks_control_plane_egress_mode_type import EKSControlPlaneEgressModeType


class EKSVpcConfigResponse(BaseModel):
    subnetIds: list[StrictStr] | None = None
    securityGroupIds: list[StrictStr] | None = None
    clusterSecurityGroupId: StrictStr | None = None
    vpcId: StrictStr | None = None
    endpointPublicAccess: StrictBool | None = None
    endpointPrivateAccess: StrictBool | None = None
    publicAccessCidrs: list[StrictStr] | None = None
    controlPlaneEgressMode: EKSControlPlaneEgressModeType | None = None
