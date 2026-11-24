from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_import_source import CloudFrontImportSource
from .cloud_front_tags import CloudFrontTags


class CloudFrontCreateKeyValueStoreRequest(BaseModel):
    Name: StrictStr
    Comment: StrictStr | None = None
    ImportSource: CloudFrontImportSource | None = None
    Tags: CloudFrontTags | None = None
