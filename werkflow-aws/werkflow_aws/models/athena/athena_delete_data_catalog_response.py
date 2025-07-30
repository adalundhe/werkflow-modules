from pydantic import BaseModel
from .athena_data_catalog import AthenaDataCatalog


class AthenaDeleteDataCatalogResponse(BaseModel):
    DataCatalog: AthenaDataCatalog