from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_app_specification import SageMakerAppSpecification
from .sage_maker_experiment_config import SageMakerExperimentConfig
from .sage_maker_network_config import SageMakerNetworkConfig
from .sage_maker_processing_input import SageMakerProcessingInput
from .sage_maker_processing_job_status import SageMakerProcessingJobStatus
from .sage_maker_processing_output_config import SageMakerProcessingOutputConfig
from .sage_maker_processing_resources import SageMakerProcessingResources
from .sage_maker_processing_stopping_condition import SageMakerProcessingStoppingCondition


class SageMakerDescribeProcessingJobResponse(BaseModel):
    ProcessingInputs: list[SageMakerProcessingInput] | None = None
    ProcessingOutputConfig: SageMakerProcessingOutputConfig | None = None
    ProcessingJobName: StrictStr | None = None
    ProcessingResources: SageMakerProcessingResources | None = None
    StoppingCondition: SageMakerProcessingStoppingCondition | None = None
    AppSpecification: SageMakerAppSpecification | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
    NetworkConfig: SageMakerNetworkConfig | None = None
    RoleArn: StrictStr | None = None
    ExperimentConfig: SageMakerExperimentConfig | None = None
    ProcessingJobArn: StrictStr | None = None
    ProcessingJobStatus: SageMakerProcessingJobStatus | None = None
    ExitMessage: StrictStr | None = None
    FailureReason: StrictStr | None = None
    ProcessingEndTime: datetime.datetime | None = None
    ProcessingStartTime: datetime.datetime | None = None
    LastModifiedTime: datetime.datetime | None = None
    CreationTime: datetime.datetime | None = None
    MonitoringScheduleArn: StrictStr | None = None
    AutoMLJobArn: StrictStr | None = None
    TrainingJobArn: StrictStr | None = None
