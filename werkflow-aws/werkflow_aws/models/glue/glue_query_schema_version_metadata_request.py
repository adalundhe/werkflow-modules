from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_metadata_key_value_pair import GlueMetadataKeyValuePair
from .glue_schema_id import GlueSchemaId
from .glue_schema_version_number import GlueSchemaVersionNumber


class GlueQuerySchemaVersionMetadataRequest(BaseModel):
    SchemaId: GlueSchemaId | None = None
    SchemaVersionNumber: GlueSchemaVersionNumber | None = None
    SchemaVersionId: StrictStr | None = None
    MetadataList: list[GlueMetadataKeyValuePair] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
