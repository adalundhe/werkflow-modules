from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchEksMetadata(BaseModel):
    labels: dict[StrictStr, StrictStr] | None = None
    annotations: dict[StrictStr, StrictStr] | None = None
    namespace: StrictStr | None = None
