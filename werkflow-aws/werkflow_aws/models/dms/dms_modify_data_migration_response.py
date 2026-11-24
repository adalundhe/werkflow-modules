from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dms_data_migration import DMSDataMigration


class DMSModifyDataMigrationResponse(BaseModel):
    DataMigration: DMSDataMigration | None = None
    ResponseMetadata: dict[str, Any] | None = None
