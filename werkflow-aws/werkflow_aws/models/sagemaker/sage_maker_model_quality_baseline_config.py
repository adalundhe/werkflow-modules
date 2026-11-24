from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_monitoring_constraints_resource import SageMakerMonitoringConstraintsResource


class SageMakerModelQualityBaselineConfig(BaseModel):
    BaseliningJobName: StrictStr | None = None
    ConstraintsResource: SageMakerMonitoringConstraintsResource | None = None
