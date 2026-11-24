from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_extension_configuration import ConnectExtensionConfiguration


class ConnectUpdateAttachedFilesConfigurationRequest(BaseModel):
    InstanceId: StrictStr
    AttachmentScope: Literal['EMAIL', 'CHAT', 'CASE', 'TASK']
    MaximumSizeLimitInBytes: StrictInt | None = None
    ExtensionConfiguration: ConnectExtensionConfiguration | None = None
