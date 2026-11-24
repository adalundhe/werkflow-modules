from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_model_explainability_app_specification import SageMakerModelExplainabilityAppSpecification
from .sage_maker_model_explainability_baseline_config import SageMakerModelExplainabilityBaselineConfig
from .sage_maker_model_explainability_job_input import SageMakerModelExplainabilityJobInput
from .sage_maker_monitoring_network_config import SageMakerMonitoringNetworkConfig
from .sage_maker_monitoring_output_config import SageMakerMonitoringOutputConfig
from .sage_maker_monitoring_resources import SageMakerMonitoringResources
from .sage_maker_monitoring_stopping_condition import SageMakerMonitoringStoppingCondition


class SageMakerDescribeModelExplainabilityJobDefinitionResponse(BaseModel):
    JobDefinitionArn: StrictStr | None = None
    JobDefinitionName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ModelExplainabilityBaselineConfig: SageMakerModelExplainabilityBaselineConfig | None = None
    ModelExplainabilityAppSpecification: SageMakerModelExplainabilityAppSpecification | None = None
    ModelExplainabilityJobInput: SageMakerModelExplainabilityJobInput | None = None
    ModelExplainabilityJobOutputConfig: SageMakerMonitoringOutputConfig | None = None
    JobResources: SageMakerMonitoringResources | None = None
    NetworkConfig: SageMakerMonitoringNetworkConfig | None = None
    RoleArn: StrictStr | None = None
    StoppingCondition: SageMakerMonitoringStoppingCondition | None = None
    ResponseMetadata: dict[str, Any] | None = None
