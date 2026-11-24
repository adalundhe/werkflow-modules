from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchMigrationSource(BaseModel):
    datasourceArn: StrictStr | None = None
