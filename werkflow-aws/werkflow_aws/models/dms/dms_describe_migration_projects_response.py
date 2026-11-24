from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_migration_project import DMSMigrationProject


class DMSDescribeMigrationProjectsResponse(BaseModel):
    Marker: StrictStr | None = None
    MigrationProjects: list[DMSMigrationProject] | None = None
    ResponseMetadata: dict[str, Any] | None = None
