from __future__ import annotations
from pydantic import BaseModel
from .ssm_azure_subscription import SSMAzureSubscription


class SSMConfigurationTargets(BaseModel):
    Subscriptions: list[SSMAzureSubscription] | None = None
