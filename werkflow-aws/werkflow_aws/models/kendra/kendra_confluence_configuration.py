from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_confluence_attachment_configuration import KendraConfluenceAttachmentConfiguration
from .kendra_confluence_blog_configuration import KendraConfluenceBlogConfiguration
from .kendra_confluence_page_configuration import KendraConfluencePageConfiguration
from .kendra_confluence_space_configuration import KendraConfluenceSpaceConfiguration
from .kendra_data_source_vpc_configuration import KendraDataSourceVpcConfiguration
from .kendra_proxy_configuration import KendraProxyConfiguration


class KendraConfluenceConfiguration(BaseModel):
    ServerUrl: StrictStr | None = None
    SecretArn: StrictStr | None = None
    Version: StrictStr | None = None
    SpaceConfiguration: KendraConfluenceSpaceConfiguration | None = None
    PageConfiguration: KendraConfluencePageConfiguration | None = None
    BlogConfiguration: KendraConfluenceBlogConfiguration | None = None
    AttachmentConfiguration: KendraConfluenceAttachmentConfiguration | None = None
    VpcConfiguration: KendraDataSourceVpcConfiguration | None = None
    InclusionPatterns: list[StrictStr] | None = None
    ExclusionPatterns: list[StrictStr] | None = None
    ProxyConfiguration: KendraProxyConfiguration | None = None
    AuthenticationType: StrictStr | None = None
