from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class IssueLayoutItemPayload(BaseModel):
    itemKey: ProjectCreateResourceIdentifier | None = None
    properties: dict[StrictStr, Any] | None = None
    sectionType: StrictStr | None = None
    type: StrictStr | None = None
