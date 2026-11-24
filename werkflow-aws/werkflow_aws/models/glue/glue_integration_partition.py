from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueIntegrationPartition(BaseModel):
    FieldName: StrictStr | None = None
    FunctionSpec: StrictStr | None = None
    ConversionSpec: StrictStr | None = None
