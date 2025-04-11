from pydantic import BaseModel, StrictStr


class DumpOptions(BaseModel):
    time_format: StrictStr