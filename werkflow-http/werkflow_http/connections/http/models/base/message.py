from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, StrictInt, StrictStr


class Message(BaseModel):
    host: Optional[StrictStr] = None
    port: Optional[StrictInt] = None
    error: Optional[StrictStr] = None

    def to_data(self) -> dict[str, Any]:
        return {
            name: value
            for name, value in self.__dict__.items()
            if value is not None
        }
