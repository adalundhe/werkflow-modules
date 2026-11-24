from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool
from .data_pipeline_validation_error import DataPipelineValidationError
from .data_pipeline_validation_warning import DataPipelineValidationWarning


class DataPipelinePutPipelineDefinitionResponse(BaseModel):
    validationErrors: list[DataPipelineValidationError] | None = None
    validationWarnings: list[DataPipelineValidationWarning] | None = None
    errored: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
