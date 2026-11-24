from __future__ import annotations
from pydantic import BaseModel
from .eks_provisioned_control_plane_tier import EKSProvisionedControlPlaneTier


class EKSControlPlaneScalingConfig(BaseModel):
    tier: EKSProvisionedControlPlaneTier | None = None
