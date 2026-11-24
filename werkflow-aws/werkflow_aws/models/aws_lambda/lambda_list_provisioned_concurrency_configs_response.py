from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lambda_provisioned_concurrency_config_list_item import LambdaProvisionedConcurrencyConfigListItem


class LambdaListProvisionedConcurrencyConfigsResponse(BaseModel):
    ProvisionedConcurrencyConfigs: list[LambdaProvisionedConcurrencyConfigListItem] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
