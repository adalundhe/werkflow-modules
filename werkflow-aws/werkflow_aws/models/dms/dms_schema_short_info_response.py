from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSSchemaShortInfoResponse(BaseModel):
    SchemaId: StrictStr | None = None
    SchemaName: StrictStr | None = None
    DatabaseId: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    DatabaseIpAddress: StrictStr | None = None
