from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_control_plane_placement_request import EKSControlPlanePlacementRequest
from .eks_etcd_placement_request import EKSEtcdPlacementRequest


class EKSOutpostConfigRequest(BaseModel):
    outpostArns: list[StrictStr]
    controlPlaneInstanceType: StrictStr
    controlPlanePlacement: EKSControlPlanePlacementRequest | None = None
    etcdInstanceType: StrictStr | None = None
    etcdPlacement: EKSEtcdPlacementRequest | None = None
