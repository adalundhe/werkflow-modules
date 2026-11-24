from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class BoardColumnPayload(BaseModel):
    maximumIssueConstraint: StrictInt | None = None
    minimumIssueConstraint: StrictInt | None = None
    name: StrictStr | None = None
    statusIds: list[ProjectCreateResourceIdentifier] | None = None
