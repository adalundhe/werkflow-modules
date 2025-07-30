from pydantic import BaseModel
from .athena_named_query import AthenaNamedQuery


class AthenaGetNamedQueryResponse(BaseModel):
    NamedQuery: AthenaNamedQuery