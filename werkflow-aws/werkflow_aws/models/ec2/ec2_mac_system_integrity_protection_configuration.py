from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2MacSystemIntegrityProtectionConfiguration(BaseModel):
    AppleInternal: StrictStr | None = None
    BaseSystem: StrictStr | None = None
    DebuggingRestrictions: StrictStr | None = None
    DTraceRestrictions: StrictStr | None = None
    FilesystemProtections: StrictStr | None = None
    KextSigning: StrictStr | None = None
    NvramProtections: StrictStr | None = None
    Status: StrictStr | None = None
