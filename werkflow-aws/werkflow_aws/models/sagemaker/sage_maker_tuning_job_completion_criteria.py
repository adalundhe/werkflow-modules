from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .sage_maker_best_objective_not_improving import SageMakerBestObjectiveNotImproving
from .sage_maker_convergence_detected import SageMakerConvergenceDetected


class SageMakerTuningJobCompletionCriteria(BaseModel):
    TargetObjectiveMetricValue: StrictFloat | StrictInt | None = None
    BestObjectiveNotImproving: SageMakerBestObjectiveNotImproving | None = None
    ConvergenceDetected: SageMakerConvergenceDetected | None = None
