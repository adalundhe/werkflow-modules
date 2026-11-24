from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectViewVersionSummary(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Description: StrictStr | None = None
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Version: StrictInt | None = None
    VersionDescription: StrictStr | None = None
