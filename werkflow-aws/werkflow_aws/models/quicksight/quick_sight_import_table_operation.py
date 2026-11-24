from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_import_table_operation_source import QuickSightImportTableOperationSource


class QuickSightImportTableOperation(BaseModel):
    Alias: StrictStr | None = None
    Source: QuickSightImportTableOperationSource | None = None
