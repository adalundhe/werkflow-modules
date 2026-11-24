from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_app_specification_model import SageMakerAppSpecificationModel
from .sage_maker_experiment_config_model import SageMakerExperimentConfigModel
from .sage_maker_network_config_model import SageMakerNetworkConfigModel
from .sage_maker_processing_input_model import SageMakerProcessingInputModel
from .sage_maker_processing_output_config_model import SageMakerProcessingOutputConfigModel
from .sage_maker_processing_resources_model import SageMakerProcessingResourcesModel
from .sage_maker_processing_stopping_condition_model import SageMakerProcessingStoppingConditionModel
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateProcessingJobRequest(BaseModel):
    ProcessingJobName: StrictStr
    ProcessingResources: SageMakerProcessingResourcesModel
    AppSpecification: SageMakerAppSpecificationModel
    RoleArn: StrictStr
    ProcessingInputs: list[SageMakerProcessingInputModel] | None = None
    ProcessingOutputConfig: SageMakerProcessingOutputConfigModel | None = None
    StoppingCondition: SageMakerProcessingStoppingConditionModel | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
    NetworkConfig: SageMakerNetworkConfigModel | None = None
    Tags: list[SageMakerTagModel] | None = None
    ExperimentConfig: SageMakerExperimentConfigModel | None = None
