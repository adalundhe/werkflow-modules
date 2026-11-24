from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_configuration_details import IoTConfigurationDetails


class IoTDescribeEncryptionConfigurationResponse(BaseModel):
    encryptionType: StrictStr | None = None
    kmsKeyArn: StrictStr | None = None
    kmsAccessRoleArn: StrictStr | None = None
    configurationDetails: IoTConfigurationDetails | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
