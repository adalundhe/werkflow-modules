from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightMappedDataSetParameter(BaseModel):
    DataSetIdentifier: StrictStr | None = None
    DataSetParameterName: StrictStr | None = None
