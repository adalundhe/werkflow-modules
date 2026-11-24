from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .el_bv2_administrative_override import ELBv2AdministrativeOverride
from .el_bv2_anomaly_detection import ELBv2AnomalyDetection
from .el_bv2_target_description import ELBv2TargetDescription
from .el_bv2_target_health import ELBv2TargetHealth


class ELBv2TargetHealthDescription(BaseModel):
    Target: ELBv2TargetDescription | None = None
    HealthCheckPort: StrictStr | None = None
    TargetHealth: ELBv2TargetHealth | None = None
    AnomalyDetection: ELBv2AnomalyDetection | None = None
    AdministrativeOverride: ELBv2AdministrativeOverride | None = None
