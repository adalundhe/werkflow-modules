from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field
from .app_flow_lambda_connector_provisioning_config import AppFlowLambdaConnectorProvisioningConfig


class AppFlowConnectorProvisioningConfig(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    lambda_: AppFlowLambdaConnectorProvisioningConfig | None = Field(default=None, alias='lambda')
