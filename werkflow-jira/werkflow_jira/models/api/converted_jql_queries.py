from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jql_query_with_unknown_users import JQLQueryWithUnknownUsers


class ConvertedJQLQueries(BaseModel):
    queriesWithUnknownUsers: list[JQLQueryWithUnknownUsers] | None = None
    queryStrings: list[StrictStr] | None = None
