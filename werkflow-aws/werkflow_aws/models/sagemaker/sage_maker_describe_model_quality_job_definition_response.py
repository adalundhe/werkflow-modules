from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_model_quality_app_specification import SageMakerModelQualityAppSpecification
from .sage_maker_model_quality_baseline_config import SageMakerModelQualityBaselineConfig
from .sage_maker_model_quality_job_input import SageMakerModelQualityJobInput
from .sage_maker_monitoring_network_config import SageMakerMonitoringNetworkConfig
from .sage_maker_monitoring_output_config import SageMakerMonitoringOutputConfig
from .sage_maker_monitoring_resources import SageMakerMonitoringResources
from .sage_maker_monitoring_stopping_condition import SageMakerMonitoringStoppingCondition


class SageMakerDescribeModelQualityJobDefinitionResponse(BaseModel):
    JobDefinitionArn: StrictStr | None = None
    JobDefinitionName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ModelQualityBaselineConfig: SageMakerModelQualityBaselineConfig | None = None
    ModelQualityAppSpecification: SageMakerModelQualityAppSpecification | None = None
    ModelQualityJobInput: SageMakerModelQualityJobInput | None = None
    ModelQualityJobOutputConfig: SageMakerMonitoringOutputConfig | None = None
    JobResources: SageMakerMonitoringResources | None = None
    NetworkConfig: SageMakerMonitoringNetworkConfig | None = None
    RoleArn: StrictStr | None = None
    StoppingCondition: SageMakerMonitoringStoppingCondition | None = None
    ResponseMetadata: dict[str, Any] | None = None
