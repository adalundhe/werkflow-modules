from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_data_quality_app_specification import SageMakerDataQualityAppSpecification
from .sage_maker_data_quality_baseline_config import SageMakerDataQualityBaselineConfig
from .sage_maker_data_quality_job_input import SageMakerDataQualityJobInput
from .sage_maker_monitoring_network_config import SageMakerMonitoringNetworkConfig
from .sage_maker_monitoring_output_config import SageMakerMonitoringOutputConfig
from .sage_maker_monitoring_resources import SageMakerMonitoringResources
from .sage_maker_monitoring_stopping_condition import SageMakerMonitoringStoppingCondition
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateDataQualityJobDefinitionRequest(BaseModel):
    JobDefinitionName: StrictStr
    DataQualityAppSpecification: SageMakerDataQualityAppSpecification
    DataQualityJobInput: SageMakerDataQualityJobInput
    DataQualityJobOutputConfig: SageMakerMonitoringOutputConfig
    JobResources: SageMakerMonitoringResources
    RoleArn: StrictStr
    DataQualityBaselineConfig: SageMakerDataQualityBaselineConfig | None = None
    NetworkConfig: SageMakerMonitoringNetworkConfig | None = None
    StoppingCondition: SageMakerMonitoringStoppingCondition | None = None
    Tags: list[SageMakerTagModel] | None = None
