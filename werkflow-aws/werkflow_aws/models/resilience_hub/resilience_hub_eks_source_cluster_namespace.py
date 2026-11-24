from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubEksSourceClusterNamespace(BaseModel):
    eksClusterArn: StrictStr | None = None
    namespace: StrictStr | None = None
