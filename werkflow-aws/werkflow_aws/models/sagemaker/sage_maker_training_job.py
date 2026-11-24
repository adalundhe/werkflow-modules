from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .sage_maker_algorithm_specification_model import SageMakerAlgorithmSpecificationModel
from .sage_maker_channel_model import SageMakerChannelModel
from .sage_maker_checkpoint_config_model import SageMakerCheckpointConfigModel
from .sage_maker_debug_hook_config_model import SageMakerDebugHookConfigModel
from .sage_maker_debug_rule_configuration_model import SageMakerDebugRuleConfigurationModel
from .sage_maker_debug_rule_evaluation_status_model import SageMakerDebugRuleEvaluationStatusModel
from .sage_maker_experiment_config_model import SageMakerExperimentConfigModel
from .sage_maker_metric_data_model import SageMakerMetricDataModel
from .sage_maker_model_artifacts_model import SageMakerModelArtifactsModel
from .sage_maker_model_package_config_model import SageMakerModelPackageConfigModel
from .sage_maker_output_data_config_model import SageMakerOutputDataConfigModel
from .sage_maker_profiler_config_model import SageMakerProfilerConfigModel
from .sage_maker_resource_config_model import SageMakerResourceConfigModel
from .sage_maker_retry_strategy_model import SageMakerRetryStrategyModel
from .sage_maker_secondary_status_transition_model import SageMakerSecondaryStatusTransitionModel
from .sage_maker_stopping_condition_model import SageMakerStoppingConditionModel
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_tensor_board_output_config_model import SageMakerTensorBoardOutputConfigModel
from .sage_maker_vpc_config_model import SageMakerVpcConfigModel
from .sage_maker_warm_pool_status_model import SageMakerWarmPoolStatusModel


class SageMakerTrainingJob(BaseModel):
    TrainingJobName: StrictStr | None = None
    TrainingJobArn: StrictStr | None = None
    TuningJobArn: StrictStr | None = None
    LabelingJobArn: StrictStr | None = None
    AutoMLJobArn: StrictStr | None = None
    ModelArtifacts: SageMakerModelArtifactsModel | None = None
    TrainingJobStatus: StrictStr | None = None
    SecondaryStatus: StrictStr | None = None
    FailureReason: StrictStr | None = None
    HyperParameters: dict[StrictStr, StrictStr] | None = None
    AlgorithmSpecification: SageMakerAlgorithmSpecificationModel | None = None
    RoleArn: StrictStr | None = None
    InputDataConfig: list[SageMakerChannelModel] | None = None
    OutputDataConfig: SageMakerOutputDataConfigModel | None = None
    ResourceConfig: SageMakerResourceConfigModel | None = None
    WarmPoolStatus: SageMakerWarmPoolStatusModel | None = None
    VpcConfig: SageMakerVpcConfigModel | None = None
    StoppingCondition: SageMakerStoppingConditionModel | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    TrainingStartTime: datetime.datetime | StrictStr | None = None
    TrainingEndTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    SecondaryStatusTransitions: list[SageMakerSecondaryStatusTransitionModel] | None = None
    FinalMetricDataList: list[SageMakerMetricDataModel] | None = None
    EnableNetworkIsolation: StrictBool | None = None
    EnableInterContainerTrafficEncryption: StrictBool | None = None
    EnableManagedSpotTraining: StrictBool | None = None
    CheckpointConfig: SageMakerCheckpointConfigModel | None = None
    TrainingTimeInSeconds: StrictInt | None = None
    BillableTimeInSeconds: StrictInt | None = None
    DebugHookConfig: SageMakerDebugHookConfigModel | None = None
    ExperimentConfig: SageMakerExperimentConfigModel | None = None
    DebugRuleConfigurations: list[SageMakerDebugRuleConfigurationModel] | None = None
    TensorBoardOutputConfig: SageMakerTensorBoardOutputConfigModel | None = None
    DebugRuleEvaluationStatuses: list[SageMakerDebugRuleEvaluationStatusModel] | None = None
    OutputModelPackageArn: StrictStr | None = None
    ModelPackageConfig: SageMakerModelPackageConfigModel | None = None
    ProfilerConfig: SageMakerProfilerConfigModel | None = None
    Environment: dict[StrictStr, StrictStr] | None = None
    RetryStrategy: SageMakerRetryStrategyModel | None = None
    Tags: list[SageMakerTagModel] | None = None
