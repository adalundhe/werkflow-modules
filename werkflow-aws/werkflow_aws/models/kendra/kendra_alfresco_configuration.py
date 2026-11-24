from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .kendra_data_source_to_index_field_mapping import KendraDataSourceToIndexFieldMapping
from .kendra_data_source_vpc_configuration import KendraDataSourceVpcConfiguration
from .kendra_s3_path import KendraS3Path


class KendraAlfrescoConfiguration(BaseModel):
    SiteUrl: StrictStr | None = None
    SiteId: StrictStr | None = None
    SecretArn: StrictStr | None = None
    SslCertificateS3Path: KendraS3Path | None = None
    CrawlSystemFolders: StrictBool | None = None
    CrawlComments: StrictBool | None = None
    EntityFilter: list[StrictStr] | None = None
    DocumentLibraryFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    BlogFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    WikiFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    InclusionPatterns: list[StrictStr] | None = None
    ExclusionPatterns: list[StrictStr] | None = None
    VpcConfiguration: KendraDataSourceVpcConfiguration | None = None
