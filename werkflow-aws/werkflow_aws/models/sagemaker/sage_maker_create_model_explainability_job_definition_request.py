from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_model_explainability_app_specification import SageMakerModelExplainabilityAppSpecification
from .sage_maker_model_explainability_baseline_config import SageMakerModelExplainabilityBaselineConfig
from .sage_maker_model_explainability_job_input import SageMakerModelExplainabilityJobInput
from .sage_maker_monitoring_network_config import SageMakerMonitoringNetworkConfig
from .sage_maker_monitoring_output_config import SageMakerMonitoringOutputConfig
from .sage_maker_monitoring_resources import SageMakerMonitoringResources
from .sage_maker_monitoring_stopping_condition import SageMakerMonitoringStoppingCondition
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateModelExplainabilityJobDefinitionRequest(BaseModel):
    JobDefinitionName: StrictStr
    ModelExplainabilityAppSpecification: SageMakerModelExplainabilityAppSpecification
    ModelExplainabilityJobInput: SageMakerModelExplainabilityJobInput
    ModelExplainabilityJobOutputConfig: SageMakerMonitoringOutputConfig
    JobResources: SageMakerMonitoringResources
    RoleArn: StrictStr
    ModelExplainabilityBaselineConfig: SageMakerModelExplainabilityBaselineConfig | None = None
    NetworkConfig: SageMakerMonitoringNetworkConfig | None = None
    StoppingCondition: SageMakerMonitoringStoppingCondition | None = None
    Tags: list[SageMakerTagModel] | None = None
