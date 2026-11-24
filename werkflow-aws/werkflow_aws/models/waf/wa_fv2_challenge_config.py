from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_immunity_time_property import WAFv2ImmunityTimeProperty


class WAFv2ChallengeConfig(BaseModel):
    ImmunityTimeProperty: WAFv2ImmunityTimeProperty | None = None
