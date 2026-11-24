from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_control_plane_placement_response import EKSControlPlanePlacementResponse
from .eks_etcd_placement_response import EKSEtcdPlacementResponse


class EKSOutpostConfigResponse(BaseModel):
    outpostArns: list[StrictStr] | None = None
    controlPlaneInstanceType: StrictStr | None = None
    controlPlanePlacement: EKSControlPlanePlacementResponse | None = None
    etcdInstanceType: StrictStr | None = None
    etcdPlacement: EKSEtcdPlacementResponse | None = None
