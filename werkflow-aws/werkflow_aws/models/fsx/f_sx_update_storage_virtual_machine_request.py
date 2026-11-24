from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_update_svm_active_directory_configuration import FSxUpdateSvmActiveDirectoryConfiguration


class FSxUpdateStorageVirtualMachineRequest(BaseModel):
    StorageVirtualMachineId: StrictStr
    ActiveDirectoryConfiguration: FSxUpdateSvmActiveDirectoryConfiguration | None = None
    ClientRequestToken: StrictStr | None = None
    SvmAdminPassword: StrictStr | None = None
