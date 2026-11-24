from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .f_sx_create_svm_active_directory_configuration import FSxCreateSvmActiveDirectoryConfiguration
from .f_sx_tag import FSxTag


class FSxCreateStorageVirtualMachineRequest(BaseModel):
    FileSystemId: StrictStr
    Name: StrictStr
    ActiveDirectoryConfiguration: FSxCreateSvmActiveDirectoryConfiguration | None = None
    ClientRequestToken: StrictStr | None = None
    SvmAdminPassword: StrictStr | None = None
    Tags: list[FSxTag] | None = None
    RootVolumeSecurityStyle: Literal['UNIX', 'NTFS', 'MIXED'] | None = None
