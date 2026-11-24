from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_control_plane_placement_response_model import EKSControlPlanePlacementResponseModel
from .eks_etcd_placement_response_model import EKSEtcdPlacementResponseModel


class EKSOutpostConfigResponseModel(BaseModel):
    outpostArns: list[StrictStr] | None = None
    controlPlaneInstanceType: StrictStr | None = None
    controlPlanePlacement: EKSControlPlanePlacementResponseModel | None = None
    etcdInstanceType: StrictStr | None = None
    etcdPlacement: EKSEtcdPlacementResponseModel | None = None
