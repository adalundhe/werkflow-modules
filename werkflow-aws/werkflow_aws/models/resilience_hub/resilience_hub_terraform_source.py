from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubTerraformSource(BaseModel):
    s3StateFileUrl: StrictStr | None = None
