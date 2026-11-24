from __future__ import annotations
from pydantic import BaseModel
from .security_scheme_level_bean import SecuritySchemeLevelBean


class AddSecuritySchemeLevelsRequestBean(BaseModel):
    levels: list[SecuritySchemeLevelBean] | None = None
