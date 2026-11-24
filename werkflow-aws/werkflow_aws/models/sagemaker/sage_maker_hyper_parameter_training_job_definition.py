from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_channel_model import SageMakerChannelModel
from .sage_maker_checkpoint_config_model import SageMakerCheckpointConfigModel
from .sage_maker_hyper_parameter_algorithm_specification import SageMakerHyperParameterAlgorithmSpecification
from .sage_maker_hyper_parameter_tuning_job_objective import SageMakerHyperParameterTuningJobObjective
from .sage_maker_hyper_parameter_tuning_resource_config import SageMakerHyperParameterTuningResourceConfig
from .sage_maker_output_data_config_model import SageMakerOutputDataConfigModel
from .sage_maker_parameter_ranges import SageMakerParameterRanges
from .sage_maker_resource_config_model import SageMakerResourceConfigModel
from .sage_maker_retry_strategy_model import SageMakerRetryStrategyModel
from .sage_maker_stopping_condition_model import SageMakerStoppingConditionModel
from .sage_maker_vpc_config_model import SageMakerVpcConfigModel


class SageMakerHyperParameterTrainingJobDefinition(BaseModel):
    DefinitionName: StrictStr | None = None
    TuningObjective: SageMakerHyperParameterTuningJobObjective | None = None
    HyperParameterRanges: SageMakerParameterRanges | None = None
    StaticHyperParameters: dict[StrictStr, StrictStr] | None = None
    AlgorithmSpecification: SageMakerHyperParameterAlgorithmSpecification | None = None
    RoleArn: StrictStr | None = None
    InputDataConfig: list[SageMakerChannelModel] | None = None
    VpcConfig: SageMakerVpcConfigModel | None = None
    OutputDataConfig: SageMakerOutputDataConfigModel | None = None
    ResourceConfig: SageMakerResourceConfigModel | None = None
    HyperParameterTuningResourceConfig: SageMakerHyperParameterTuningResourceConfig | None = None
    StoppingCondition: SageMakerStoppingConditionModel | None = None
    EnableNetworkIsolation: StrictBool | None = None
    EnableInterContainerTrafficEncryption: StrictBool | None = None
    EnableManagedSpotTraining: StrictBool | None = None
    CheckpointConfig: SageMakerCheckpointConfigModel | None = None
    RetryStrategy: SageMakerRetryStrategyModel | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
