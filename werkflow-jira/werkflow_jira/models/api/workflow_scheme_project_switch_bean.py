from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr
from .mappings_by_issue_type_override import MappingsByIssueTypeOverride


class WorkflowSchemeProjectSwitchBean(BaseModel):
    model_config = ConfigDict(extra="allow")

    mappingsByIssueTypeOverride: list[MappingsByIssueTypeOverride] | None = None
    projectId: StrictStr | None = None
    targetSchemeId: StrictStr | None = None
