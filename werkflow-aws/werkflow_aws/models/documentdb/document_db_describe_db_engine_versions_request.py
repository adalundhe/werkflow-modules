from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .document_db_filter import DocumentDBFilter


class DocumentDBDescribeDBEngineVersionsRequest(BaseModel):
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    DBParameterGroupFamily: StrictStr | None = None
    Filters: list[DocumentDBFilter] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
    DefaultOnly: StrictBool | None = None
    ListSupportedCharacterSets: StrictBool | None = None
    ListSupportedTimezones: StrictBool | None = None
