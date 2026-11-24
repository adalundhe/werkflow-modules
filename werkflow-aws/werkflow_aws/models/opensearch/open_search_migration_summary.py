from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .open_search_migration_error import OpenSearchMigrationError
from .open_search_migration_source import OpenSearchMigrationSource


class OpenSearchMigrationSummary(BaseModel):
    migrationId: StrictStr | None = None
    status: StrictStr | None = None
    applicationId: StrictStr | None = None
    source: OpenSearchMigrationSource | None = None
    exportedCount: StrictInt | None = None
    importedCount: StrictInt | None = None
    error: OpenSearchMigrationError | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
