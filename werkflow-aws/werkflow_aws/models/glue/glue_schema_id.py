from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueSchemaId(BaseModel):
    SchemaArn: StrictStr | None = None
    SchemaName: StrictStr | None = None
    RegistryName: StrictStr | None = None
