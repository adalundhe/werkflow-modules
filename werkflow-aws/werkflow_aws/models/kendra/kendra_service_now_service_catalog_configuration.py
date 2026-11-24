from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .kendra_data_source_to_index_field_mapping import KendraDataSourceToIndexFieldMapping


class KendraServiceNowServiceCatalogConfiguration(BaseModel):
    CrawlAttachments: StrictBool | None = None
    IncludeAttachmentFilePatterns: list[StrictStr] | None = None
    ExcludeAttachmentFilePatterns: list[StrictStr] | None = None
    DocumentDataFieldName: StrictStr | None = None
    DocumentTitleFieldName: StrictStr | None = None
    FieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
