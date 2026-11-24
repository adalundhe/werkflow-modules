from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruAmazonCodeGuruProfilerIntegration(BaseModel):
    Status: StrictStr | None = None
