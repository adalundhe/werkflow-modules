from __future__ import annotations
from pydantic import BaseModel
from .security_hub_aws_open_search_service_domain_log_publishing_option import SecurityHubAwsOpenSearchServiceDomainLogPublishingOption


class SecurityHubAwsOpenSearchServiceDomainLogPublishingOptionsDetails(BaseModel):
    IndexSlowLogs: SecurityHubAwsOpenSearchServiceDomainLogPublishingOption | None = None
    SearchSlowLogs: SecurityHubAwsOpenSearchServiceDomainLogPublishingOption | None = None
    AuditLogs: SecurityHubAwsOpenSearchServiceDomainLogPublishingOption | None = None
