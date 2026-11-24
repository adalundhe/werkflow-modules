from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_migration_summary import OpenSearchMigrationSummary


class OpenSearchListMigrationsResponse(BaseModel):
    migrations: list[OpenSearchMigrationSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
