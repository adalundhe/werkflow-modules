from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .kendra_confluence_space_to_index_field_mapping import KendraConfluenceSpaceToIndexFieldMapping


class KendraConfluenceSpaceConfiguration(BaseModel):
    CrawlPersonalSpaces: StrictBool | None = None
    CrawlArchivedSpaces: StrictBool | None = None
    IncludeSpaces: list[StrictStr] | None = None
    ExcludeSpaces: list[StrictStr] | None = None
    SpaceFieldMappings: list[KendraConfluenceSpaceToIndexFieldMapping] | None = None
