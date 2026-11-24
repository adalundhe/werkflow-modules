from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .glue_table_input import GlueTableInput
from .glue_update_open_table_format_input import GlueUpdateOpenTableFormatInput


class GlueUpdateTableRequest(BaseModel):
    DatabaseName: StrictStr
    CatalogId: StrictStr | None = None
    Name: StrictStr | None = None
    TableInput: GlueTableInput | None = None
    SkipArchive: StrictBool | None = None
    TransactionId: StrictStr | None = None
    VersionId: StrictStr | None = None
    ViewUpdateAction: Literal['ADD', 'REPLACE', 'ADD_OR_REPLACE', 'DROP'] | None = None
    Force: StrictBool | None = None
    UpdateOpenTableFormatInput: GlueUpdateOpenTableFormatInput | None = None
