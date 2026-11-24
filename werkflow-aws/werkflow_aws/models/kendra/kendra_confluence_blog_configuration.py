from __future__ import annotations
from pydantic import BaseModel
from .kendra_confluence_blog_to_index_field_mapping import KendraConfluenceBlogToIndexFieldMapping


class KendraConfluenceBlogConfiguration(BaseModel):
    BlogFieldMappings: list[KendraConfluenceBlogToIndexFieldMapping] | None = None
