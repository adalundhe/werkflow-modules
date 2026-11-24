from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_pipeline_parameter_value import DataPipelineParameterValue


class DataPipelineActivatePipelineRequest(BaseModel):
    pipelineId: StrictStr
    parameterValues: list[DataPipelineParameterValue] | None = None
    startTimestamp: datetime.datetime | StrictStr | None = None
