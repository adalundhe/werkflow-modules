from typing import Optional

from pydantic import BaseModel, StrictStr


class Metadata(BaseModel):
    protocol: Optional[StrictStr] = None
