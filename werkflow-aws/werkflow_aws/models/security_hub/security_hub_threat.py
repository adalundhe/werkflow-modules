from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_file_paths import SecurityHubFilePaths


class SecurityHubThreat(BaseModel):
    Name: StrictStr | None = None
    Severity: StrictStr | None = None
    ItemCount: StrictInt | None = None
    FilePaths: list[SecurityHubFilePaths] | None = None
