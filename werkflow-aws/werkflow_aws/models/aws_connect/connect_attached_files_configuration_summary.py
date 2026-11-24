from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_extension_configuration import ConnectExtensionConfiguration


class ConnectAttachedFilesConfigurationSummary(BaseModel):
    InstanceId: StrictStr | None = None
    AttachmentScope: StrictStr | None = None
    MaximumSizeLimitInBytes: StrictInt | None = None
    ExtensionConfiguration: ConnectExtensionConfiguration | None = None
