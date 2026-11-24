from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_test_connection_input import GlueTestConnectionInput


class GlueTestConnectionRequest(BaseModel):
    ConnectionName: StrictStr | None = None
    CatalogId: StrictStr | None = None
    TestConnectionInput: GlueTestConnectionInput | None = None
