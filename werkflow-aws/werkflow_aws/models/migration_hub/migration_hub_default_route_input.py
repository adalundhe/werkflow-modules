from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class MigrationHubDefaultRouteInput(BaseModel):
    ActivationState: Literal['ACTIVE', 'INACTIVE'] | None = None
