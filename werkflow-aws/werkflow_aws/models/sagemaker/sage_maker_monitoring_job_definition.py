from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_monitoring_app_specification import SageMakerMonitoringAppSpecification
from .sage_maker_monitoring_baseline_config import SageMakerMonitoringBaselineConfig
from .sage_maker_monitoring_input import SageMakerMonitoringInput
from .sage_maker_monitoring_output_config import SageMakerMonitoringOutputConfig
from .sage_maker_monitoring_resources import SageMakerMonitoringResources
from .sage_maker_monitoring_stopping_condition import SageMakerMonitoringStoppingCondition
from .sage_maker_network_config_model import SageMakerNetworkConfigModel


class SageMakerMonitoringJobDefinition(BaseModel):
    BaselineConfig: SageMakerMonitoringBaselineConfig | None = None
    MonitoringInputs: list[SageMakerMonitoringInput] | None = None
    MonitoringOutputConfig: SageMakerMonitoringOutputConfig | None = None
    MonitoringResources: SageMakerMonitoringResources | None = None
    MonitoringAppSpecification: SageMakerMonitoringAppSpecification | None = None
    StoppingCondition: SageMakerMonitoringStoppingCondition | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
    NetworkConfig: SageMakerNetworkConfigModel | None = None
    RoleArn: StrictStr | None = None
