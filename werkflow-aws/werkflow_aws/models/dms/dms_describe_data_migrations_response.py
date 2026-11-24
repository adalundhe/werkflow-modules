from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_data_migration import DMSDataMigration


class DMSDescribeDataMigrationsResponse(BaseModel):
    DataMigrations: list[DMSDataMigration] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
