from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_service_now_knowledge_article_configuration import KendraServiceNowKnowledgeArticleConfiguration
from .kendra_service_now_service_catalog_configuration import KendraServiceNowServiceCatalogConfiguration


class KendraServiceNowConfiguration(BaseModel):
    HostUrl: StrictStr | None = None
    SecretArn: StrictStr | None = None
    ServiceNowBuildVersion: StrictStr | None = None
    KnowledgeArticleConfiguration: KendraServiceNowKnowledgeArticleConfiguration | None = None
    ServiceCatalogConfiguration: KendraServiceNowServiceCatalogConfiguration | None = None
    AuthenticationType: StrictStr | None = None
