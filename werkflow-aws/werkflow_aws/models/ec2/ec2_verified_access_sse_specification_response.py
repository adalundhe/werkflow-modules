from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2VerifiedAccessSseSpecificationResponse(BaseModel):
    CustomerManagedKeyEnabled: StrictBool | None = None
    KmsKeyArn: StrictStr | None = None
