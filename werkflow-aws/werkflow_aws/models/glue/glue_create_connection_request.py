from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_connection_input import GlueConnectionInput


class GlueCreateConnectionRequest(BaseModel):
    ConnectionInput: GlueConnectionInput
    CatalogId: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
