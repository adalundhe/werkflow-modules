from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_auto_ml_candidate_step import SageMakerAutoMLCandidateStep
from .sage_maker_auto_ml_container_definition import SageMakerAutoMLContainerDefinition
from .sage_maker_candidate_properties import SageMakerCandidateProperties
from .sage_maker_final_auto_ml_job_objective_metric import SageMakerFinalAutoMLJobObjectiveMetric


class SageMakerAutoMLCandidate(BaseModel):
    CandidateName: StrictStr | None = None
    FinalAutoMLJobObjectiveMetric: SageMakerFinalAutoMLJobObjectiveMetric | None = None
    ObjectiveStatus: StrictStr | None = None
    CandidateSteps: list[SageMakerAutoMLCandidateStep] | None = None
    CandidateStatus: StrictStr | None = None
    InferenceContainers: list[SageMakerAutoMLContainerDefinition] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    CandidateProperties: SageMakerCandidateProperties | None = None
    InferenceContainerDefinitions: dict[StrictStr, list[SageMakerAutoMLContainerDefinition]] | None = None
