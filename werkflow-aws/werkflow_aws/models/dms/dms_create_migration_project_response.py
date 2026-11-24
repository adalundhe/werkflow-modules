from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dms_migration_project import DMSMigrationProject


class DMSCreateMigrationProjectResponse(BaseModel):
    MigrationProject: DMSMigrationProject | None = None
    ResponseMetadata: dict[str, Any] | None = None
