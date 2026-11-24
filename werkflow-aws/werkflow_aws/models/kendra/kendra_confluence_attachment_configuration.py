from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .kendra_confluence_attachment_to_index_field_mapping import KendraConfluenceAttachmentToIndexFieldMapping


class KendraConfluenceAttachmentConfiguration(BaseModel):
    CrawlAttachments: StrictBool | None = None
    AttachmentFieldMappings: list[KendraConfluenceAttachmentToIndexFieldMapping] | None = None
