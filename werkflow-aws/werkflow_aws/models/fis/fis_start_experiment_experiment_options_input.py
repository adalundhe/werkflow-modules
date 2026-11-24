from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class FISStartExperimentExperimentOptionsInput(BaseModel):
    actionsMode: Literal['skip-all', 'run-all'] | None = None
