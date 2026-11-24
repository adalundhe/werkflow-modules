from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .glue_column_row_filter import GlueColumnRowFilter
from .glue_table_model import GlueTableModel


class GlueGetUnfilteredTableMetadataResponse(BaseModel):
    Table: GlueTableModel | None = None
    AuthorizedColumns: list[StrictStr] | None = None
    IsRegisteredWithLakeFormation: StrictBool | None = None
    CellFilters: list[GlueColumnRowFilter] | None = None
    QueryAuthorizationId: StrictStr | None = None
    IsMultiDialectView: StrictBool | None = None
    IsMaterializedView: StrictBool | None = None
    ResourceArn: StrictStr | None = None
    IsProtected: StrictBool | None = None
    Permissions: list[StrictStr] | None = None
    RowFilter: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
