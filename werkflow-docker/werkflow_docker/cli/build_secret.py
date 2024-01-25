from pydantic import (
    BaseModel,
    StrictStr
)


class BuildSecret(BaseModel):
    secret_id: StrictStr
    source: StrictStr

    def to_string(self):
        return f'id={self.secret_id},src={self.source}'