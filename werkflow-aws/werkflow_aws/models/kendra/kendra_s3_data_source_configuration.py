from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_access_control_list_configuration import KendraAccessControlListConfiguration
from .kendra_documents_metadata_configuration import KendraDocumentsMetadataConfiguration


class KendraS3DataSourceConfiguration(BaseModel):
    BucketName: StrictStr | None = None
    InclusionPrefixes: list[StrictStr] | None = None
    InclusionPatterns: list[StrictStr] | None = None
    ExclusionPatterns: list[StrictStr] | None = None
    DocumentsMetadataConfiguration: KendraDocumentsMetadataConfiguration | None = None
    AccessControlListConfiguration: KendraAccessControlListConfiguration | None = None
