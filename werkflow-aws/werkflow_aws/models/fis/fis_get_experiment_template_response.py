from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .fis_experiment_template import FISExperimentTemplate


class FISGetExperimentTemplateResponse(BaseModel):
    experimentTemplate: FISExperimentTemplate | None = None
    ResponseMetadata: dict[str, Any] | None = None
