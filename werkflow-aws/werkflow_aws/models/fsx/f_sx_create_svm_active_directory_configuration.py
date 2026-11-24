from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_self_managed_active_directory_configuration import FSxSelfManagedActiveDirectoryConfiguration


class FSxCreateSvmActiveDirectoryConfiguration(BaseModel):
    NetBiosName: StrictStr
    SelfManagedActiveDirectoryConfiguration: FSxSelfManagedActiveDirectoryConfiguration | None = None
