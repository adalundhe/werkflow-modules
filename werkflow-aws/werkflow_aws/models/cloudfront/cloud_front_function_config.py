from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_key_value_store_associations import CloudFrontKeyValueStoreAssociations


class CloudFrontFunctionConfig(BaseModel):
    Comment: StrictStr | None = None
    Runtime: StrictStr | None = None
    KeyValueStoreAssociations: CloudFrontKeyValueStoreAssociations | None = None
