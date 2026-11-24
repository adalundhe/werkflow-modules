from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_model_bias_app_specification import SageMakerModelBiasAppSpecification
from .sage_maker_model_bias_baseline_config import SageMakerModelBiasBaselineConfig
from .sage_maker_model_bias_job_input import SageMakerModelBiasJobInput
from .sage_maker_monitoring_network_config import SageMakerMonitoringNetworkConfig
from .sage_maker_monitoring_output_config import SageMakerMonitoringOutputConfig
from .sage_maker_monitoring_resources import SageMakerMonitoringResources
from .sage_maker_monitoring_stopping_condition import SageMakerMonitoringStoppingCondition
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateModelBiasJobDefinitionRequest(BaseModel):
    JobDefinitionName: StrictStr
    ModelBiasAppSpecification: SageMakerModelBiasAppSpecification
    ModelBiasJobInput: SageMakerModelBiasJobInput
    ModelBiasJobOutputConfig: SageMakerMonitoringOutputConfig
    JobResources: SageMakerMonitoringResources
    RoleArn: StrictStr
    ModelBiasBaselineConfig: SageMakerModelBiasBaselineConfig | None = None
    NetworkConfig: SageMakerMonitoringNetworkConfig | None = None
    StoppingCondition: SageMakerMonitoringStoppingCondition | None = None
    Tags: list[SageMakerTagModel] | None = None
