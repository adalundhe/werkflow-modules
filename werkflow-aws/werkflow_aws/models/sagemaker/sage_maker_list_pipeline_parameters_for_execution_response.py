from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_parameter_model import SageMakerParameterModel


class SageMakerListPipelineParametersForExecutionResponse(BaseModel):
    PipelineParameters: list[SageMakerParameterModel] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
