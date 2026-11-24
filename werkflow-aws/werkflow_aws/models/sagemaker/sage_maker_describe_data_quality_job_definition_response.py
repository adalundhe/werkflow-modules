from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_data_quality_app_specification import SageMakerDataQualityAppSpecification
from .sage_maker_data_quality_baseline_config import SageMakerDataQualityBaselineConfig
from .sage_maker_data_quality_job_input import SageMakerDataQualityJobInput
from .sage_maker_monitoring_network_config import SageMakerMonitoringNetworkConfig
from .sage_maker_monitoring_output_config import SageMakerMonitoringOutputConfig
from .sage_maker_monitoring_resources import SageMakerMonitoringResources
from .sage_maker_monitoring_stopping_condition import SageMakerMonitoringStoppingCondition


class SageMakerDescribeDataQualityJobDefinitionResponse(BaseModel):
    JobDefinitionArn: StrictStr | None = None
    JobDefinitionName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    DataQualityBaselineConfig: SageMakerDataQualityBaselineConfig | None = None
    DataQualityAppSpecification: SageMakerDataQualityAppSpecification | None = None
    DataQualityJobInput: SageMakerDataQualityJobInput | None = None
    DataQualityJobOutputConfig: SageMakerMonitoringOutputConfig | None = None
    JobResources: SageMakerMonitoringResources | None = None
    NetworkConfig: SageMakerMonitoringNetworkConfig | None = None
    RoleArn: StrictStr | None = None
    StoppingCondition: SageMakerMonitoringStoppingCondition | None = None
    ResponseMetadata: dict[str, Any] | None = None
