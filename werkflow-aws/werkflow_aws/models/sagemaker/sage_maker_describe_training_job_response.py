from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .sage_maker_algorithm_specification import SageMakerAlgorithmSpecification
from .sage_maker_channel import SageMakerChannel
from .sage_maker_checkpoint_config import SageMakerCheckpointConfig
from .sage_maker_debug_hook_config import SageMakerDebugHookConfig
from .sage_maker_debug_rule_configuration import SageMakerDebugRuleConfiguration
from .sage_maker_debug_rule_evaluation_status import SageMakerDebugRuleEvaluationStatus
from .sage_maker_experiment_config import SageMakerExperimentConfig
from .sage_maker_infra_check_config import SageMakerInfraCheckConfig
from .sage_maker_metric_data import SageMakerMetricData
from .sage_maker_mlflow_config import SageMakerMlflowConfig
from .sage_maker_mlflow_details import SageMakerMlflowDetails
from .sage_maker_model_artifacts import SageMakerModelArtifacts
from .sage_maker_model_package_config import SageMakerModelPackageConfig
from .sage_maker_output_data_config import SageMakerOutputDataConfig
from .sage_maker_profiler_config import SageMakerProfilerConfig
from .sage_maker_profiler_rule_configuration import SageMakerProfilerRuleConfiguration
from .sage_maker_profiler_rule_evaluation_status import SageMakerProfilerRuleEvaluationStatus
from .sage_maker_profiling_status import SageMakerProfilingStatus
from .sage_maker_remote_debug_config import SageMakerRemoteDebugConfig
from .sage_maker_resource_config import SageMakerResourceConfig
from .sage_maker_retry_strategy import SageMakerRetryStrategy
from .sage_maker_secondary_status import SageMakerSecondaryStatus
from .sage_maker_secondary_status_transition import SageMakerSecondaryStatusTransition
from .sage_maker_serverless_job_config import SageMakerServerlessJobConfig
from .sage_maker_stopping_condition import SageMakerStoppingCondition
from .sage_maker_tensor_board_output_config import SageMakerTensorBoardOutputConfig
from .sage_maker_training_job_status import SageMakerTrainingJobStatus
from .sage_maker_training_progress_info import SageMakerTrainingProgressInfo
from .sage_maker_vpc_config import SageMakerVpcConfig
from .sage_maker_warm_pool_status import SageMakerWarmPoolStatus


class SageMakerDescribeTrainingJobResponse(BaseModel):
    TrainingJobName: StrictStr | None = None
    TrainingJobArn: StrictStr | None = None
    TuningJobArn: StrictStr | None = None
    LabelingJobArn: StrictStr | None = None
    AutoMLJobArn: StrictStr | None = None
    ModelArtifacts: SageMakerModelArtifacts | None = None
    TrainingJobStatus: SageMakerTrainingJobStatus | None = None
    SecondaryStatus: SageMakerSecondaryStatus | None = None
    FailureReason: StrictStr | None = None
    HyperParameters: dict[StrictStr, StrictStr] | None = None
    AlgorithmSpecification: SageMakerAlgorithmSpecification | None = None
    RoleArn: StrictStr | None = None
    InputDataConfig: list[SageMakerChannel] | None = None
    OutputDataConfig: SageMakerOutputDataConfig | None = None
    ResourceConfig: SageMakerResourceConfig | None = None
    WarmPoolStatus: SageMakerWarmPoolStatus | None = None
    VpcConfig: SageMakerVpcConfig | None = None
    StoppingCondition: SageMakerStoppingCondition | None = None
    CreationTime: datetime.datetime | None = None
    TrainingStartTime: datetime.datetime | None = None
    TrainingEndTime: datetime.datetime | None = None
    LastModifiedTime: datetime.datetime | None = None
    SecondaryStatusTransitions: list[SageMakerSecondaryStatusTransition] | None = None
    FinalMetricDataList: list[SageMakerMetricData] | None = None
    EnableNetworkIsolation: StrictBool | None = None
    EnableInterContainerTrafficEncryption: StrictBool | None = None
    EnableManagedSpotTraining: StrictBool | None = None
    CheckpointConfig: SageMakerCheckpointConfig | None = None
    TrainingTimeInSeconds: StrictInt | None = None
    BillableTimeInSeconds: StrictInt | None = None
    BillableTokenCount: StrictInt | None = None
    DebugHookConfig: SageMakerDebugHookConfig | None = None
    ExperimentConfig: SageMakerExperimentConfig | None = None
    DebugRuleConfigurations: list[SageMakerDebugRuleConfiguration] | None = None
    TensorBoardOutputConfig: SageMakerTensorBoardOutputConfig | None = None
    DebugRuleEvaluationStatuses: list[SageMakerDebugRuleEvaluationStatus] | None = None
    ProfilerConfig: SageMakerProfilerConfig | None = None
    ProfilerRuleConfigurations: list[SageMakerProfilerRuleConfiguration] | None = None
    ProfilerRuleEvaluationStatuses: list[SageMakerProfilerRuleEvaluationStatus] | None = None
    ProfilingStatus: SageMakerProfilingStatus | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
    RetryStrategy: SageMakerRetryStrategy | None = None
    RemoteDebugConfig: SageMakerRemoteDebugConfig | None = None
    InfraCheckConfig: SageMakerInfraCheckConfig | None = None
    ServerlessJobConfig: SageMakerServerlessJobConfig | None = None
    MlflowConfig: SageMakerMlflowConfig | None = None
    ModelPackageConfig: SageMakerModelPackageConfig | None = None
    MlflowDetails: SageMakerMlflowDetails | None = None
    ProgressInfo: SageMakerTrainingProgressInfo | None = None
    OutputModelPackageArn: StrictStr | None = None
