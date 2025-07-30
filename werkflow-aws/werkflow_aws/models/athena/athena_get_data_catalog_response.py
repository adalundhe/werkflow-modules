from pydantic import BaseModel
from .athena_data_catalog import AthenaDataCatalog


class AthenaGetDataCatalogResponse(BaseModel):
    DataCatalog: AthenaDataCatalog