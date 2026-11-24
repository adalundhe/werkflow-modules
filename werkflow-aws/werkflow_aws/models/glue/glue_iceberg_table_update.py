from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .glue_iceberg_encrypted_key import GlueIcebergEncryptedKey
from .glue_iceberg_partition_spec import GlueIcebergPartitionSpec
from .glue_iceberg_schema import GlueIcebergSchema
from .glue_iceberg_sort_order import GlueIcebergSortOrder


class GlueIcebergTableUpdate(BaseModel):
    Schema: GlueIcebergSchema
    Location: StrictStr
    PartitionSpec: GlueIcebergPartitionSpec | None = None
    SortOrder: GlueIcebergSortOrder | None = None
    Properties: dict[StrictStr, StrictStr] | None = None
    Action: Literal['add-schema', 'set-current-schema', 'add-spec', 'set-default-spec', 'add-sort-order', 'set-default-sort-order', 'set-location', 'set-properties', 'remove-properties', 'add-encryption-key', 'remove-encryption-key'] | None = None
    EncryptionKey: GlueIcebergEncryptedKey | None = None
    KeyId: StrictStr | None = None
