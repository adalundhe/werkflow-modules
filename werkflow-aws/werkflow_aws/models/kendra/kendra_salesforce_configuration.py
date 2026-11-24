from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .kendra_salesforce_chatter_feed_configuration import KendraSalesforceChatterFeedConfiguration
from .kendra_salesforce_knowledge_article_configuration import KendraSalesforceKnowledgeArticleConfiguration
from .kendra_salesforce_standard_object_attachment_configuration import KendraSalesforceStandardObjectAttachmentConfiguration
from .kendra_salesforce_standard_object_configuration import KendraSalesforceStandardObjectConfiguration


class KendraSalesforceConfiguration(BaseModel):
    ServerUrl: StrictStr | None = None
    SecretArn: StrictStr | None = None
    StandardObjectConfigurations: list[KendraSalesforceStandardObjectConfiguration] | None = None
    KnowledgeArticleConfiguration: KendraSalesforceKnowledgeArticleConfiguration | None = None
    ChatterFeedConfiguration: KendraSalesforceChatterFeedConfiguration | None = None
    CrawlAttachments: StrictBool | None = None
    StandardObjectAttachmentConfiguration: KendraSalesforceStandardObjectAttachmentConfiguration | None = None
    IncludeAttachmentFilePatterns: list[StrictStr] | None = None
    ExcludeAttachmentFilePatterns: list[StrictStr] | None = None
