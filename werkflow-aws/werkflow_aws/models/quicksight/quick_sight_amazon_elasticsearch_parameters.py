from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAmazonElasticsearchParameters(BaseModel):
    Domain: StrictStr | None = None
