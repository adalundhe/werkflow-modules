from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_migration_options import OpenSearchMigrationOptions


class OpenSearchStartMigrationRequest(BaseModel):
    applicationId: StrictStr
    migrationOptions: OpenSearchMigrationOptions
    clientToken: StrictStr | None = None
