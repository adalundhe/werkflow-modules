from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_data_catalog_summary import AthenaDataCatalogSummary


class AthenaListDataCatalogsResponse(BaseModel):
    DataCatalogsSummary: list[AthenaDataCatalogSummary]
    NextToken: StrictStr | None = None