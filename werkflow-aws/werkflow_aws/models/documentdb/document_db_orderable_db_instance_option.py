from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .document_db_availability_zone import DocumentDBAvailabilityZone


class DocumentDBOrderableDBInstanceOption(BaseModel):
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    DBInstanceClass: StrictStr | None = None
    LicenseModel: StrictStr | None = None
    AvailabilityZones: list[DocumentDBAvailabilityZone] | None = None
    Vpc: StrictBool | None = None
    StorageType: StrictStr | None = None
