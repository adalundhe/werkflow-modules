from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetUserDefinedFunctionRequest(BaseModel):
    DatabaseName: StrictStr
    FunctionName: StrictStr
    CatalogId: StrictStr | None = None
