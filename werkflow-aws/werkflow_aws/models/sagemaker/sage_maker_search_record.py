from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_endpoint import SageMakerEndpoint
from .sage_maker_experiment import SageMakerExperiment
from .sage_maker_feature_group import SageMakerFeatureGroup
from .sage_maker_feature_metadata import SageMakerFeatureMetadata
from .sage_maker_hub_content import SageMakerHubContent
from .sage_maker_hyper_parameter_tuning_job_search_entity import SageMakerHyperParameterTuningJobSearchEntity
from .sage_maker_job import SageMakerJob
from .sage_maker_model_card import SageMakerModelCard
from .sage_maker_model_dashboard_model import SageMakerModelDashboardModel
from .sage_maker_model_package import SageMakerModelPackage
from .sage_maker_model_package_group import SageMakerModelPackageGroup
from .sage_maker_pipeline import SageMakerPipeline
from .sage_maker_pipeline_execution import SageMakerPipelineExecution
from .sage_maker_pipeline_version import SageMakerPipelineVersion
from .sage_maker_project import SageMakerProject
from .sage_maker_training_job import SageMakerTrainingJob
from .sage_maker_trial import SageMakerTrial
from .sage_maker_trial_component import SageMakerTrialComponent


class SageMakerSearchRecord(BaseModel):
    TrainingJob: SageMakerTrainingJob | None = None
    Experiment: SageMakerExperiment | None = None
    Trial: SageMakerTrial | None = None
    TrialComponent: SageMakerTrialComponent | None = None
    Endpoint: SageMakerEndpoint | None = None
    ModelPackage: SageMakerModelPackage | None = None
    ModelPackageGroup: SageMakerModelPackageGroup | None = None
    Pipeline: SageMakerPipeline | None = None
    PipelineExecution: SageMakerPipelineExecution | None = None
    PipelineVersion: SageMakerPipelineVersion | None = None
    FeatureGroup: SageMakerFeatureGroup | None = None
    FeatureMetadata: SageMakerFeatureMetadata | None = None
    Project: SageMakerProject | None = None
    HyperParameterTuningJob: SageMakerHyperParameterTuningJobSearchEntity | None = None
    ModelCard: SageMakerModelCard | None = None
    Model: SageMakerModelDashboardModel | None = None
    Job: SageMakerJob | None = None
    HubContent: SageMakerHubContent | None = None
