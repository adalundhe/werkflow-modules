from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessFipsEndpoints(BaseModel):
    collectionEndpoint: StrictStr | None = None
    dashboardEndpoint: StrictStr | None = None
