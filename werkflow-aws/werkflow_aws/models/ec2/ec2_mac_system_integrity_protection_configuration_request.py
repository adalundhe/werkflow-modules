from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class EC2MacSystemIntegrityProtectionConfigurationRequest(BaseModel):
    AppleInternal: Literal['enabled', 'disabled'] | None = None
    BaseSystem: Literal['enabled', 'disabled'] | None = None
    DebuggingRestrictions: Literal['enabled', 'disabled'] | None = None
    DTraceRestrictions: Literal['enabled', 'disabled'] | None = None
    FilesystemProtections: Literal['enabled', 'disabled'] | None = None
    KextSigning: Literal['enabled', 'disabled'] | None = None
    NvramProtections: Literal['enabled', 'disabled'] | None = None
