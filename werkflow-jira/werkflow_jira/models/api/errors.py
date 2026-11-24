from __future__ import annotations
from pydantic import BaseModel
from .error import Error


class Errors(BaseModel):
    issueIsSubtask: Error | None = None
    issuesInArchivedProjects: Error | None = None
    issuesInUnlicensedProjects: Error | None = None
    issuesNotFound: Error | None = None
    userDoesNotHavePermission: Error | None = None
