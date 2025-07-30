from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_prepared_statement import AthenaPreparedStatement


class AthenaListPreparedStatementsResponse(BaseModel):
    PreparedStatements: list[AthenaPreparedStatement]
    NextToken: StrictStr | None = None