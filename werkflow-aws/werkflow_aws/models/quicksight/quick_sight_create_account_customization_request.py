from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_account_customization import QuickSightAccountCustomization
from .quick_sight_tag import QuickSightTag


class QuickSightCreateAccountCustomizationRequest(BaseModel):
    AwsAccountId: StrictStr
    AccountCustomization: QuickSightAccountCustomization
    Namespace: StrictStr | None = None
    Tags: list[QuickSightTag] | None = None
