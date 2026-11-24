from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class FISCreateExperimentTemplateExperimentOptionsInput(BaseModel):
    accountTargeting: Literal['single-account', 'multi-account'] | None = None
    emptyTargetResolutionMode: Literal['fail', 'skip'] | None = None
