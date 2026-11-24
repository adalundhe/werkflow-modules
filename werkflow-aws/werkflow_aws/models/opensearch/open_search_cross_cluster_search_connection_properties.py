from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchCrossClusterSearchConnectionProperties(BaseModel):
    SkipUnavailable: StrictStr | None = None
