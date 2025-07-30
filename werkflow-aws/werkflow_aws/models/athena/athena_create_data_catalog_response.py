from pydantic import BaseModel
from .athena_data_catalog import AthenaDataCatalog


class AthenaCreateDataCatalogResponse(BaseModel):
    DataCatalog: AthenaDataCatalog