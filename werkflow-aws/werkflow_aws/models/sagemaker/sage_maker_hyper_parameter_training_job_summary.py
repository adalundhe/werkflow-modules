from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_final_hyper_parameter_tuning_job_objective_metric import SageMakerFinalHyperParameterTuningJobObjectiveMetric


class SageMakerHyperParameterTrainingJobSummary(BaseModel):
    TrainingJobDefinitionName: StrictStr | None = None
    TrainingJobName: StrictStr | None = None
    TrainingJobArn: StrictStr | None = None
    TuningJobName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    TrainingStartTime: datetime.datetime | StrictStr | None = None
    TrainingEndTime: datetime.datetime | StrictStr | None = None
    TrainingJobStatus: StrictStr | None = None
    TunedHyperParameters: dict[StrictStr, StrictStr] | None = None
    FailureReason: StrictStr | None = None
    FinalHyperParameterTuningJobObjectiveMetric: SageMakerFinalHyperParameterTuningJobObjectiveMetric | None = None
    ObjectiveStatus: StrictStr | None = None
