from pydantic import (
    BaseModel,
    StrictStr,
)
from .athena_prepared_statement import AthenaPreparedStatement


class AthenaListPreparedStatementsResponse(BaseModel):
    PreparedStatements: list[AthenaPreparedStatement] | None = None
    NextToken: StrictStr | None = None
