from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_model_bias_app_specification import SageMakerModelBiasAppSpecification
from .sage_maker_model_bias_baseline_config import SageMakerModelBiasBaselineConfig
from .sage_maker_model_bias_job_input import SageMakerModelBiasJobInput
from .sage_maker_monitoring_network_config import SageMakerMonitoringNetworkConfig
from .sage_maker_monitoring_output_config import SageMakerMonitoringOutputConfig
from .sage_maker_monitoring_resources import SageMakerMonitoringResources
from .sage_maker_monitoring_stopping_condition import SageMakerMonitoringStoppingCondition


class SageMakerDescribeModelBiasJobDefinitionResponse(BaseModel):
    JobDefinitionArn: StrictStr | None = None
    JobDefinitionName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ModelBiasBaselineConfig: SageMakerModelBiasBaselineConfig | None = None
    ModelBiasAppSpecification: SageMakerModelBiasAppSpecification | None = None
    ModelBiasJobInput: SageMakerModelBiasJobInput | None = None
    ModelBiasJobOutputConfig: SageMakerMonitoringOutputConfig | None = None
    JobResources: SageMakerMonitoringResources | None = None
    NetworkConfig: SageMakerMonitoringNetworkConfig | None = None
    RoleArn: StrictStr | None = None
    StoppingCondition: SageMakerMonitoringStoppingCondition | None = None
    ResponseMetadata: dict[str, Any] | None = None
