from __future__ import annotations
from pydantic import BaseModel
from .issue_type_hierarchy_payload import IssueTypeHierarchyPayload
from .issue_type_payload import IssueTypePayload
from .issue_type_scheme_payload import IssueTypeSchemePayload


class IssueTypeProjectCreatePayload(BaseModel):
    issueTypeHierarchy: list[IssueTypeHierarchyPayload] | None = None
    issueTypeScheme: IssueTypeSchemePayload | None = None
    issueTypes: list[IssueTypePayload] | None = None
