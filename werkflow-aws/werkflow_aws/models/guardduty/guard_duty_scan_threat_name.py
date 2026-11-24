from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_scan_file_path import GuardDutyScanFilePath


class GuardDutyScanThreatName(BaseModel):
    Name: StrictStr | None = None
    Severity: StrictStr | None = None
    ItemCount: StrictInt | None = None
    FilePaths: list[GuardDutyScanFilePath] | None = None
