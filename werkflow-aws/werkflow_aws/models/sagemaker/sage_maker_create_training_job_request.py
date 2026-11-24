from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_algorithm_specification import SageMakerAlgorithmSpecification
from .sage_maker_channel import SageMakerChannel
from .sage_maker_checkpoint_config import SageMakerCheckpointConfig
from .sage_maker_debug_hook_config import SageMakerDebugHookConfig
from .sage_maker_debug_rule_configuration import SageMakerDebugRuleConfiguration
from .sage_maker_experiment_config import SageMakerExperimentConfig
from .sage_maker_infra_check_config import SageMakerInfraCheckConfig
from .sage_maker_mlflow_config import SageMakerMlflowConfig
from .sage_maker_model_package_config import SageMakerModelPackageConfig
from .sage_maker_output_data_config import SageMakerOutputDataConfig
from .sage_maker_profiler_config import SageMakerProfilerConfig
from .sage_maker_profiler_rule_configuration import SageMakerProfilerRuleConfiguration
from .sage_maker_remote_debug_config import SageMakerRemoteDebugConfig
from .sage_maker_resource_config import SageMakerResourceConfig
from .sage_maker_retry_strategy import SageMakerRetryStrategy
from .sage_maker_serverless_job_config import SageMakerServerlessJobConfig
from .sage_maker_session_chaining_config import SageMakerSessionChainingConfig
from .sage_maker_stopping_condition import SageMakerStoppingCondition
from .sage_maker_tag import SageMakerTag
from .sage_maker_tensor_board_output_config import SageMakerTensorBoardOutputConfig
from .sage_maker_vpc_config import SageMakerVpcConfig


class SageMakerCreateTrainingJobRequest(BaseModel):
    TrainingJobName: StrictStr
    RoleArn: StrictStr
    OutputDataConfig: SageMakerOutputDataConfig
    HyperParameters: dict[StrictStr, StrictStr] | None = None
    AlgorithmSpecification: SageMakerAlgorithmSpecification | None = None
    InputDataConfig: list[SageMakerChannel] | None = None
    ResourceConfig: SageMakerResourceConfig | None = None
    VpcConfig: SageMakerVpcConfig | None = None
    StoppingCondition: SageMakerStoppingCondition | None = None
    Tags: list[SageMakerTag] | None = None
    EnableNetworkIsolation: StrictBool | None = None
    EnableInterContainerTrafficEncryption: StrictBool | None = None
    EnableManagedSpotTraining: StrictBool | None = None
    CheckpointConfig: SageMakerCheckpointConfig | None = None
    DebugHookConfig: SageMakerDebugHookConfig | None = None
    DebugRuleConfigurations: list[SageMakerDebugRuleConfiguration] | None = None
    TensorBoardOutputConfig: SageMakerTensorBoardOutputConfig | None = None
    ExperimentConfig: SageMakerExperimentConfig | None = None
    ProfilerConfig: SageMakerProfilerConfig | None = None
    ProfilerRuleConfigurations: list[SageMakerProfilerRuleConfiguration] | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
    RetryStrategy: SageMakerRetryStrategy | None = None
    RemoteDebugConfig: SageMakerRemoteDebugConfig | None = None
    InfraCheckConfig: SageMakerInfraCheckConfig | None = None
    SessionChainingConfig: SageMakerSessionChainingConfig | None = None
    ServerlessJobConfig: SageMakerServerlessJobConfig | None = None
    MlflowConfig: SageMakerMlflowConfig | None = None
    ModelPackageConfig: SageMakerModelPackageConfig | None = None
