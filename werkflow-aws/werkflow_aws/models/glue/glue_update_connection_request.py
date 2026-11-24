from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_connection_input import GlueConnectionInput


class GlueUpdateConnectionRequest(BaseModel):
    Name: StrictStr
    ConnectionInput: GlueConnectionInput
    CatalogId: StrictStr | None = None
