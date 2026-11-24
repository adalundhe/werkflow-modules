from __future__ import annotations
from pydantic import BaseModel
from .ssm_azure_configuration import SSMAzureConfiguration
from .ssm_gcp_configuration import SSMGcpConfiguration


class SSMCloudConnectorConfiguration(BaseModel):
    AzureConfiguration: SSMAzureConfiguration | None = None
    GcpConfiguration: SSMGcpConfiguration | None = None
