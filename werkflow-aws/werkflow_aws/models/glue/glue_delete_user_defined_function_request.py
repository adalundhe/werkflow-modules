from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteUserDefinedFunctionRequest(BaseModel):
    DatabaseName: StrictStr
    FunctionName: StrictStr
    CatalogId: StrictStr | None = None
