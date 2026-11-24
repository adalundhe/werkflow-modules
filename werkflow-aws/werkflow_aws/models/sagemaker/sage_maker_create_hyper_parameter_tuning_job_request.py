from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_autotune import SageMakerAutotune
from .sage_maker_hyper_parameter_training_job_definition import SageMakerHyperParameterTrainingJobDefinition
from .sage_maker_hyper_parameter_tuning_job_config import SageMakerHyperParameterTuningJobConfig
from .sage_maker_hyper_parameter_tuning_job_warm_start_config import SageMakerHyperParameterTuningJobWarmStartConfig
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateHyperParameterTuningJobRequest(BaseModel):
    HyperParameterTuningJobName: StrictStr
    HyperParameterTuningJobConfig: SageMakerHyperParameterTuningJobConfig
    TrainingJobDefinition: SageMakerHyperParameterTrainingJobDefinition | None = None
    TrainingJobDefinitions: list[SageMakerHyperParameterTrainingJobDefinition] | None = None
    WarmStartConfig: SageMakerHyperParameterTuningJobWarmStartConfig | None = None
    Tags: list[SageMakerTagModel] | None = None
    Autotune: SageMakerAutotune | None = None
