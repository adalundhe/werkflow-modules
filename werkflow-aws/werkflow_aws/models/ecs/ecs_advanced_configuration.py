from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSAdvancedConfiguration(BaseModel):
    alternateTargetGroupArn: StrictStr | None = None
    productionListenerRule: StrictStr | None = None
    testListenerRule: StrictStr | None = None
    roleArn: StrictStr | None = None
