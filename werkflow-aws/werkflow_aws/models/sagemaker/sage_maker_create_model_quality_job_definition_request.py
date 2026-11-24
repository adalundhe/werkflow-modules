from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_model_quality_app_specification import SageMakerModelQualityAppSpecification
from .sage_maker_model_quality_baseline_config import SageMakerModelQualityBaselineConfig
from .sage_maker_model_quality_job_input import SageMakerModelQualityJobInput
from .sage_maker_monitoring_network_config import SageMakerMonitoringNetworkConfig
from .sage_maker_monitoring_output_config import SageMakerMonitoringOutputConfig
from .sage_maker_monitoring_resources import SageMakerMonitoringResources
from .sage_maker_monitoring_stopping_condition import SageMakerMonitoringStoppingCondition
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateModelQualityJobDefinitionRequest(BaseModel):
    JobDefinitionName: StrictStr
    ModelQualityAppSpecification: SageMakerModelQualityAppSpecification
    ModelQualityJobInput: SageMakerModelQualityJobInput
    ModelQualityJobOutputConfig: SageMakerMonitoringOutputConfig
    JobResources: SageMakerMonitoringResources
    RoleArn: StrictStr
    ModelQualityBaselineConfig: SageMakerModelQualityBaselineConfig | None = None
    NetworkConfig: SageMakerMonitoringNetworkConfig | None = None
    StoppingCondition: SageMakerMonitoringStoppingCondition | None = None
    Tags: list[SageMakerTagModel] | None = None
