from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .issue_layout_item_payload import IssueLayoutItemPayload
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class IssueLayoutPayload(BaseModel):
    containerId: ProjectCreateResourceIdentifier | None = None
    issueLayoutType: StrictStr | None = None
    items: list[IssueLayoutItemPayload] | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
