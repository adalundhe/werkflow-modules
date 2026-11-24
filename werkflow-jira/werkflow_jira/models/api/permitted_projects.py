from __future__ import annotations
from pydantic import BaseModel
from .project_identifier_bean import ProjectIdentifierBean


class PermittedProjects(BaseModel):
    projects: list[ProjectIdentifierBean] | None = None
