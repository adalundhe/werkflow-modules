from pydantic import BaseModel, StrictStr


class AthenaCreateNamedQueryResponse(BaseModel):
    NamedQueryId: StrictStr