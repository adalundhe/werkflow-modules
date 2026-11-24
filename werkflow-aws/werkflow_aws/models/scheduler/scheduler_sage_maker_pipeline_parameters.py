from __future__ import annotations
from pydantic import BaseModel
from .scheduler_sage_maker_pipeline_parameter import SchedulerSageMakerPipelineParameter


class SchedulerSageMakerPipelineParameters(BaseModel):
    PipelineParameterList: list[SchedulerSageMakerPipelineParameter] | None = None
