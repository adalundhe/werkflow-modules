from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr
from .status_migration import StatusMigration


class StatusMappingDTO(BaseModel):
    model_config = ConfigDict(extra="allow")

    issueTypeId: StrictStr | None = None
    projectId: StrictStr | None = None
    statusMigrations: list[StatusMigration] | None = None
