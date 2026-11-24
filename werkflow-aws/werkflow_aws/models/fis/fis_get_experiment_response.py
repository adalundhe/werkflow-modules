from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .fis_experiment import FISExperiment


class FISGetExperimentResponse(BaseModel):
    experiment: FISExperiment | None = None
    ResponseMetadata: dict[str, Any] | None = None
