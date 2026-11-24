from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .document_db_filter import DocumentDBFilter


class DocumentDBDescribeOrderableDBInstanceOptionsRequest(BaseModel):
    Engine: StrictStr
    EngineVersion: StrictStr | None = None
    DBInstanceClass: StrictStr | None = None
    LicenseModel: StrictStr | None = None
    Vpc: StrictBool | None = None
    Filters: list[DocumentDBFilter] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
