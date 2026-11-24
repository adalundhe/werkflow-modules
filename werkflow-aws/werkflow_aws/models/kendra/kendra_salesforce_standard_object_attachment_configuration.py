from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_data_source_to_index_field_mapping import KendraDataSourceToIndexFieldMapping


class KendraSalesforceStandardObjectAttachmentConfiguration(BaseModel):
    DocumentTitleFieldName: StrictStr | None = None
    FieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
