from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataPipelineInstanceIdentity(BaseModel):
    document: StrictStr | None = None
    signature: StrictStr | None = None
