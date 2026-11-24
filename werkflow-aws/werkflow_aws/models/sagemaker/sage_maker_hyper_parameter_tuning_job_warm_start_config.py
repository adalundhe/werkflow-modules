from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_parent_hyper_parameter_tuning_job import SageMakerParentHyperParameterTuningJob


class SageMakerHyperParameterTuningJobWarmStartConfig(BaseModel):
    ParentHyperParameterTuningJobs: list[SageMakerParentHyperParameterTuningJob] | None = None
    WarmStartType: StrictStr | None = None
