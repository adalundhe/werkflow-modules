from pydantic import BaseModel
from .athena_database import AthenaDatabase


class AthenaGetDatabaseResponse(BaseModel):
    Database: AthenaDatabase