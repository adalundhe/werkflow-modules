from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .document_db_filter import DocumentDBFilter


class DocumentDBDescribePendingMaintenanceActionsRequest(BaseModel):
    ResourceIdentifier: StrictStr | None = None
    Filters: list[DocumentDBFilter] | None = None
    Marker: StrictStr | None = None
    MaxRecords: StrictInt | None = None
