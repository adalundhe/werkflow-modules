from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueSchemaListItem(BaseModel):
    RegistryName: StrictStr | None = None
    SchemaName: StrictStr | None = None
    SchemaArn: StrictStr | None = None
    Description: StrictStr | None = None
    SchemaStatus: StrictStr | None = None
    CreatedTime: StrictStr | None = None
    UpdatedTime: StrictStr | None = None
