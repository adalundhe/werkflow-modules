from __future__ import annotations
from pydantic import BaseModel
from .security_hub_azure_detail import SecurityHubAzureDetail
from .security_hub_gcp_detail import SecurityHubGcpDetail
from .security_hub_jira_cloud_detail import SecurityHubJiraCloudDetail
from .security_hub_service_now_detail import SecurityHubServiceNowDetail


class SecurityHubProviderDetail(BaseModel):
    JiraCloud: SecurityHubJiraCloudDetail | None = None
    ServiceNow: SecurityHubServiceNowDetail | None = None
    Azure: SecurityHubAzureDetail | None = None
    GCP: SecurityHubGcpDetail | None = None
