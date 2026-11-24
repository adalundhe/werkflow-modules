from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubEksSource(BaseModel):
    eksClusterArn: StrictStr | None = None
    namespaces: list[StrictStr] | None = None
