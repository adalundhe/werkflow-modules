from __future__ import annotations
from pydantic import BaseModel
from .issue_entity_properties_for_multi_update import IssueEntityPropertiesForMultiUpdate


class MultiIssueEntityProperties(BaseModel):
    issues: list[IssueEntityPropertiesForMultiUpdate] | None = None
