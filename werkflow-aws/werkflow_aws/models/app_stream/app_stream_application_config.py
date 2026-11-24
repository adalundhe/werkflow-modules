from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamApplicationConfig(BaseModel):
    Name: StrictStr
    AbsoluteAppPath: StrictStr
    DisplayName: StrictStr | None = None
    AbsoluteIconPath: StrictStr | None = None
    AbsoluteManifestPath: StrictStr | None = None
    WorkingDirectory: StrictStr | None = None
    LaunchParameters: StrictStr | None = None
