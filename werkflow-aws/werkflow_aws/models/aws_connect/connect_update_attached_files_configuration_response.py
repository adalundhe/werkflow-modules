from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_extension_configuration import ConnectExtensionConfiguration


class ConnectUpdateAttachedFilesConfigurationResponse(BaseModel):
    InstanceId: StrictStr | None = None
    AttachmentScope: StrictStr | None = None
    MaximumSizeLimitInBytes: StrictInt | None = None
    ExtensionConfiguration: ConnectExtensionConfiguration | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
