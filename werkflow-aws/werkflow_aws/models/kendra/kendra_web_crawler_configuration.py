from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .kendra_authentication_configuration import KendraAuthenticationConfiguration
from .kendra_proxy_configuration import KendraProxyConfiguration
from .kendra_urls import KendraUrls


class KendraWebCrawlerConfiguration(BaseModel):
    Urls: KendraUrls | None = None
    CrawlDepth: StrictInt | None = None
    MaxLinksPerPage: StrictInt | None = None
    MaxContentSizePerPageInMegaBytes: StrictFloat | StrictInt | None = None
    MaxUrlsPerMinuteCrawlRate: StrictInt | None = None
    UrlInclusionPatterns: list[StrictStr] | None = None
    UrlExclusionPatterns: list[StrictStr] | None = None
    ProxyConfiguration: KendraProxyConfiguration | None = None
    AuthenticationConfiguration: KendraAuthenticationConfiguration | None = None
