from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class WAFv2ManagedProductDescriptor(BaseModel):
    VendorName: StrictStr | None = None
    ManagedRuleSetName: StrictStr | None = None
    ProductId: StrictStr | None = None
    ProductLink: StrictStr | None = None
    ProductTitle: StrictStr | None = None
    ProductDescription: StrictStr | None = None
    SnsTopicArn: StrictStr | None = None
    IsVersioningSupported: StrictBool | None = None
    IsAdvancedManagedRuleSet: StrictBool | None = None
