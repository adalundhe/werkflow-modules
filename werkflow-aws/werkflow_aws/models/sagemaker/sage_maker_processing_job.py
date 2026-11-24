from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_app_specification_model import SageMakerAppSpecificationModel
from .sage_maker_experiment_config_model import SageMakerExperimentConfigModel
from .sage_maker_network_config_model import SageMakerNetworkConfigModel
from .sage_maker_processing_input_model import SageMakerProcessingInputModel
from .sage_maker_processing_output_config_model import SageMakerProcessingOutputConfigModel
from .sage_maker_processing_resources_model import SageMakerProcessingResourcesModel
from .sage_maker_processing_stopping_condition_model import SageMakerProcessingStoppingConditionModel
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerProcessingJob(BaseModel):
    ProcessingInputs: list[SageMakerProcessingInputModel] | None = None
    ProcessingOutputConfig: SageMakerProcessingOutputConfigModel | None = None
    ProcessingJobName: StrictStr | None = None
    ProcessingResources: SageMakerProcessingResourcesModel | None = None
    StoppingCondition: SageMakerProcessingStoppingConditionModel | None = None
    AppSpecification: SageMakerAppSpecificationModel | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
    NetworkConfig: SageMakerNetworkConfigModel | None = None
    RoleArn: StrictStr | None = None
    ExperimentConfig: SageMakerExperimentConfigModel | None = None
    ProcessingJobArn: StrictStr | None = None
    ProcessingJobStatus: StrictStr | None = None
    ExitMessage: StrictStr | None = None
    FailureReason: StrictStr | None = None
    ProcessingEndTime: datetime.datetime | StrictStr | None = None
    ProcessingStartTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    MonitoringScheduleArn: StrictStr | None = None
    AutoMLJobArn: StrictStr | None = None
    TrainingJobArn: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
