from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .kendra_data_source_to_index_field_mapping import KendraDataSourceToIndexFieldMapping
from .kendra_data_source_vpc_configuration import KendraDataSourceVpcConfiguration
from .kendra_proxy_configuration import KendraProxyConfiguration
from .kendra_s3_path import KendraS3Path


class KendraSharePointConfiguration(BaseModel):
    SharePointVersion: StrictStr | None = None
    Urls: list[StrictStr] | None = None
    SecretArn: StrictStr | None = None
    CrawlAttachments: StrictBool | None = None
    UseChangeLog: StrictBool | None = None
    InclusionPatterns: list[StrictStr] | None = None
    ExclusionPatterns: list[StrictStr] | None = None
    VpcConfiguration: KendraDataSourceVpcConfiguration | None = None
    FieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    DocumentTitleFieldName: StrictStr | None = None
    DisableLocalGroups: StrictBool | None = None
    SslCertificateS3Path: KendraS3Path | None = None
    AuthenticationType: StrictStr | None = None
    ProxyConfiguration: KendraProxyConfiguration | None = None
