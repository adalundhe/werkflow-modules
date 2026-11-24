from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehoseSchemaConfiguration(BaseModel):
    RoleARN: StrictStr | None = None
    CatalogId: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    TableName: StrictStr | None = None
    Region: StrictStr | None = None
    VersionId: StrictStr | None = None
