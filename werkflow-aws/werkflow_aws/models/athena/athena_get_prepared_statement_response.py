from pydantic import BaseModel
from .athena_prepared_statement import AthenaPreparedStatement


class AthenaGetPreparedStatementResponse(BaseModel):
    PreparedStatement: AthenaPreparedStatement