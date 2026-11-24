from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceDescribeRetentionConfigurationsRequest(BaseModel):
    RetentionConfigurationNames: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
