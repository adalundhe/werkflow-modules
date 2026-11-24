from __future__ import annotations
from pydantic import BaseModel
from .security_hub_aws_elasticsearch_domain_log_publishing_options_log_config import SecurityHubAwsElasticsearchDomainLogPublishingOptionsLogConfig


class SecurityHubAwsElasticsearchDomainLogPublishingOptions(BaseModel):
    IndexSlowLogs: SecurityHubAwsElasticsearchDomainLogPublishingOptionsLogConfig | None = None
    SearchSlowLogs: SecurityHubAwsElasticsearchDomainLogPublishingOptionsLogConfig | None = None
    AuditLogs: SecurityHubAwsElasticsearchDomainLogPublishingOptionsLogConfig | None = None
