from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_model import SageMakerModel
from .sage_maker_model_dashboard_endpoint import SageMakerModelDashboardEndpoint
from .sage_maker_model_dashboard_model_card import SageMakerModelDashboardModelCard
from .sage_maker_model_dashboard_monitoring_schedule import SageMakerModelDashboardMonitoringSchedule
from .sage_maker_transform_job import SageMakerTransformJob


class SageMakerModelDashboardModel(BaseModel):
    Model: SageMakerModel | None = None
    Endpoints: list[SageMakerModelDashboardEndpoint] | None = None
    LastBatchTransformJob: SageMakerTransformJob | None = None
    MonitoringSchedules: list[SageMakerModelDashboardMonitoringSchedule] | None = None
    ModelCard: SageMakerModelDashboardModelCard | None = None
