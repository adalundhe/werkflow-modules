from __future__ import annotations
from pydantic import BaseModel
from .security_hub_stateless_custom_publish_metric_action import SecurityHubStatelessCustomPublishMetricAction


class SecurityHubStatelessCustomActionDefinition(BaseModel):
    PublishMetricAction: SecurityHubStatelessCustomPublishMetricAction | None = None
