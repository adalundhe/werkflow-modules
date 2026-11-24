from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class FISUpdateExperimentTemplateExperimentOptionsInput(BaseModel):
    emptyTargetResolutionMode: Literal['fail', 'skip'] | None = None
