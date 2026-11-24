from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .glue_ddbelt_catalog_additional_options import GlueDDBELTCatalogAdditionalOptions


class GlueDynamoDBCatalogSource(BaseModel):
    Name: StrictStr | None = None
    Database: StrictStr | None = None
    Table: StrictStr | None = None
    PitrEnabled: StrictBool | None = None
    AdditionalOptions: GlueDDBELTCatalogAdditionalOptions | None = None
