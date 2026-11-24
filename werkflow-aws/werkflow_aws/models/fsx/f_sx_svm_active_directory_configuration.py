from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_self_managed_active_directory_attributes import FSxSelfManagedActiveDirectoryAttributes


class FSxSvmActiveDirectoryConfiguration(BaseModel):
    NetBiosName: StrictStr | None = None
    SelfManagedActiveDirectoryConfiguration: FSxSelfManagedActiveDirectoryAttributes | None = None
