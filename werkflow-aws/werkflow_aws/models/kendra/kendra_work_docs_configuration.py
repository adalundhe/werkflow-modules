from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .kendra_data_source_to_index_field_mapping import KendraDataSourceToIndexFieldMapping


class KendraWorkDocsConfiguration(BaseModel):
    OrganizationId: StrictStr | None = None
    CrawlComments: StrictBool | None = None
    UseChangeLog: StrictBool | None = None
    InclusionPatterns: list[StrictStr] | None = None
    ExclusionPatterns: list[StrictStr] | None = None
    FieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
