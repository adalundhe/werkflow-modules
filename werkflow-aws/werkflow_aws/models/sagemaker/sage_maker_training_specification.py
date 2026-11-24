from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_additional_s3_data_source import SageMakerAdditionalS3DataSource
from .sage_maker_channel_specification import SageMakerChannelSpecification
from .sage_maker_hyper_parameter_specification import SageMakerHyperParameterSpecification
from .sage_maker_hyper_parameter_tuning_job_objective import SageMakerHyperParameterTuningJobObjective
from .sage_maker_metric_definition_model import SageMakerMetricDefinitionModel


class SageMakerTrainingSpecification(BaseModel):
    TrainingImage: StrictStr | None = None
    TrainingImageDigest: StrictStr | None = None
    SupportedHyperParameters: list[SageMakerHyperParameterSpecification] | None = None
    SupportedTrainingInstanceTypes: list[StrictStr] | None = None
    SupportsDistributedTraining: StrictBool | None = None
    MetricDefinitions: list[SageMakerMetricDefinitionModel] | None = None
    TrainingChannels: list[SageMakerChannelSpecification] | None = None
    SupportedTuningJobObjectiveMetrics: list[SageMakerHyperParameterTuningJobObjective] | None = None
    AdditionalS3DataSource: SageMakerAdditionalS3DataSource | None = None
