from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .data_zone_encryption_configuration import DataZoneEncryptionConfiguration


class DataZonePutDataExportConfigurationRequest(BaseModel):
    domainIdentifier: StrictStr
    enableExport: StrictBool
    encryptionConfiguration: DataZoneEncryptionConfiguration | None = None
    clientToken: StrictStr | None = None
