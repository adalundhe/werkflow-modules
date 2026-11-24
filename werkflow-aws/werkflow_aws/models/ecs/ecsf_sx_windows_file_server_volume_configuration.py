from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecsf_sx_windows_file_server_authorization_config import ECSFSxWindowsFileServerAuthorizationConfig


class ECSFSxWindowsFileServerVolumeConfiguration(BaseModel):
    fileSystemId: StrictStr | None = None
    rootDirectory: StrictStr | None = None
    authorizationConfig: ECSFSxWindowsFileServerAuthorizationConfig | None = None
