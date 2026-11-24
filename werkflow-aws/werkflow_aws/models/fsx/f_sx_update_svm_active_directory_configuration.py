from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_self_managed_active_directory_configuration_updates import FSxSelfManagedActiveDirectoryConfigurationUpdates


class FSxUpdateSvmActiveDirectoryConfiguration(BaseModel):
    SelfManagedActiveDirectoryConfiguration: FSxSelfManagedActiveDirectoryConfigurationUpdates | None = None
    NetBiosName: StrictStr | None = None
