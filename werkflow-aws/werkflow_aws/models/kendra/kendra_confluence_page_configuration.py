from __future__ import annotations
from pydantic import BaseModel
from .kendra_confluence_page_to_index_field_mapping import KendraConfluencePageToIndexFieldMapping


class KendraConfluencePageConfiguration(BaseModel):
    PageFieldMappings: list[KendraConfluencePageToIndexFieldMapping] | None = None
