from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_and_issue_type_pair import ProjectAndIssueTypePair


class WorkflowElementReference(BaseModel):
    propertyKey: StrictStr | None = None
    ruleId: StrictStr | None = None
    statusMappingReference: ProjectAndIssueTypePair | None = None
    statusReference: StrictStr | None = None
    transitionId: StrictStr | None = None
