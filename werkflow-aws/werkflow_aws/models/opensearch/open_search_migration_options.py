from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_export_options import OpenSearchExportOptions
from .open_search_migration_source import OpenSearchMigrationSource
from .open_search_migration_workspace import OpenSearchMigrationWorkspace


class OpenSearchMigrationOptions(BaseModel):
    source: OpenSearchMigrationSource
    workspace: OpenSearchMigrationWorkspace
    exportOptions: OpenSearchExportOptions | None = None
    conflictResolution: StrictStr | None = None
