from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_data_source_to_index_field_mapping import KendraDataSourceToIndexFieldMapping


class KendraColumnConfiguration(BaseModel):
    DocumentIdColumnName: StrictStr | None = None
    DocumentDataColumnName: StrictStr | None = None
    DocumentTitleColumnName: StrictStr | None = None
    FieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    ChangeDetectingColumns: list[StrictStr] | None = None
