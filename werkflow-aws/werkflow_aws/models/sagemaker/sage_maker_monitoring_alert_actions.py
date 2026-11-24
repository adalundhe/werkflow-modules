from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_model_dashboard_indicator_action import SageMakerModelDashboardIndicatorAction


class SageMakerMonitoringAlertActions(BaseModel):
    ModelDashboardIndicator: SageMakerModelDashboardIndicatorAction | None = None
