from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_account_customization import QuickSightAccountCustomization


class QuickSightCreateAccountCustomizationResponse(BaseModel):
    Arn: StrictStr | None = None
    AwsAccountId: StrictStr | None = None
    Namespace: StrictStr | None = None
    AccountCustomization: QuickSightAccountCustomization | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
