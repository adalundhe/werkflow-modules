from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_hyper_parameter_training_job_definition import SageMakerHyperParameterTrainingJobDefinition
from .sage_maker_hyper_parameter_training_job_summary import SageMakerHyperParameterTrainingJobSummary
from .sage_maker_hyper_parameter_tuning_job_completion_details import SageMakerHyperParameterTuningJobCompletionDetails
from .sage_maker_hyper_parameter_tuning_job_config import SageMakerHyperParameterTuningJobConfig
from .sage_maker_hyper_parameter_tuning_job_consumed_resources import SageMakerHyperParameterTuningJobConsumedResources
from .sage_maker_hyper_parameter_tuning_job_warm_start_config import SageMakerHyperParameterTuningJobWarmStartConfig
from .sage_maker_objective_status_counters import SageMakerObjectiveStatusCounters
from .sage_maker_tag_model import SageMakerTagModel
from .sage_maker_training_job_status_counters import SageMakerTrainingJobStatusCounters


class SageMakerHyperParameterTuningJobSearchEntity(BaseModel):
    HyperParameterTuningJobName: StrictStr | None = None
    HyperParameterTuningJobArn: StrictStr | None = None
    HyperParameterTuningJobConfig: SageMakerHyperParameterTuningJobConfig | None = None
    TrainingJobDefinition: SageMakerHyperParameterTrainingJobDefinition | None = None
    TrainingJobDefinitions: list[SageMakerHyperParameterTrainingJobDefinition] | None = None
    HyperParameterTuningJobStatus: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    HyperParameterTuningEndTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    TrainingJobStatusCounters: SageMakerTrainingJobStatusCounters | None = None
    ObjectiveStatusCounters: SageMakerObjectiveStatusCounters | None = None
    BestTrainingJob: SageMakerHyperParameterTrainingJobSummary | None = None
    OverallBestTrainingJob: SageMakerHyperParameterTrainingJobSummary | None = None
    WarmStartConfig: SageMakerHyperParameterTuningJobWarmStartConfig | None = None
    FailureReason: StrictStr | None = None
    TuningJobCompletionDetails: SageMakerHyperParameterTuningJobCompletionDetails | None = None
    ConsumedResources: SageMakerHyperParameterTuningJobConsumedResources | None = None
    Tags: list[SageMakerTagModel] | None = None
