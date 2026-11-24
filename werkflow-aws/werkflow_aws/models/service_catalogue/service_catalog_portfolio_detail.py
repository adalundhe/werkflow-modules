from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ServiceCatalogPortfolioDetail(BaseModel):
    Id: StrictStr | None = None
    ARN: StrictStr | None = None
    DisplayName: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    ProviderName: StrictStr | None = None
