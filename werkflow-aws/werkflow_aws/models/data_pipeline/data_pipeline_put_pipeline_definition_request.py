from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_pipeline_parameter_object import DataPipelineParameterObject
from .data_pipeline_parameter_value import DataPipelineParameterValue
from .data_pipeline_pipeline_object import DataPipelinePipelineObject


class DataPipelinePutPipelineDefinitionRequest(BaseModel):
    pipelineId: StrictStr
    pipelineObjects: list[DataPipelinePipelineObject]
    parameterObjects: list[DataPipelineParameterObject] | None = None
    parameterValues: list[DataPipelineParameterValue] | None = None
