from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_monitoring_constraints_resource import SageMakerMonitoringConstraintsResource
from .sage_maker_monitoring_statistics_resource import SageMakerMonitoringStatisticsResource


class SageMakerMonitoringBaselineConfig(BaseModel):
    BaseliningJobName: StrictStr | None = None
    ConstraintsResource: SageMakerMonitoringConstraintsResource | None = None
    StatisticsResource: SageMakerMonitoringStatisticsResource | None = None
