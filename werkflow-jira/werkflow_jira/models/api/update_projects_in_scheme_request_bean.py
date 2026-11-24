from __future__ import annotations
from pydantic import BaseModel, ConfigDict
from .priority_scheme_changes_without_mappings import PrioritySchemeChangesWithoutMappings


class UpdateProjectsInSchemeRequestBean(BaseModel):
    model_config = ConfigDict(extra="allow")

    add: PrioritySchemeChangesWithoutMappings | None = None
    remove: PrioritySchemeChangesWithoutMappings | None = None
