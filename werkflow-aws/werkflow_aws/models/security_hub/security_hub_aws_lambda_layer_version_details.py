from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsLambdaLayerVersionDetails(BaseModel):
    Version: StrictInt | None = None
    CompatibleRuntimes: list[StrictStr] | None = None
    CreatedDate: StrictStr | None = None
