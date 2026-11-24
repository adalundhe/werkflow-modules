from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .data_pipeline_parameter_object import DataPipelineParameterObject
from .data_pipeline_parameter_value import DataPipelineParameterValue
from .data_pipeline_pipeline_object import DataPipelinePipelineObject


class DataPipelineGetPipelineDefinitionResponse(BaseModel):
    pipelineObjects: list[DataPipelinePipelineObject] | None = None
    parameterObjects: list[DataPipelineParameterObject] | None = None
    parameterValues: list[DataPipelineParameterValue] | None = None
    ResponseMetadata: dict[str, Any] | None = None
