from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .mwaa_team_config import MWAATeamConfig


class MWAAUpdateTeamsInput(BaseModel):
    AddOrUpdate: dict[StrictStr, MWAATeamConfig] | None = None
    Remove: list[StrictStr] | None = None
