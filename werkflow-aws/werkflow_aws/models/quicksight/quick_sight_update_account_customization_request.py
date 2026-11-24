from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_account_customization import QuickSightAccountCustomization


class QuickSightUpdateAccountCustomizationRequest(BaseModel):
    AwsAccountId: StrictStr
    AccountCustomization: QuickSightAccountCustomization
    Namespace: StrictStr | None = None
