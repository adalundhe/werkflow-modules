from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueSchemaVersionListItem(BaseModel):
    SchemaArn: StrictStr | None = None
    SchemaVersionId: StrictStr | None = None
    VersionNumber: StrictInt | None = None
    Status: StrictStr | None = None
    CreatedTime: StrictStr | None = None
