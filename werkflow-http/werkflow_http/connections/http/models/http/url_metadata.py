from typing import Optional

from pydantic import BaseModel, StrictStr


class URLMetadata(BaseModel):
    host: Optional[StrictStr] = None
    path: Optional[StrictStr] = None
    params: Optional[StrictStr] = None
    query: Optional[StrictStr] = None
