from __future__ import annotations
from pydantic import BaseModel
from .security_level import SecurityLevel


class ProjectIssueSecurityLevels(BaseModel):
    levels: list[SecurityLevel] | None = None
