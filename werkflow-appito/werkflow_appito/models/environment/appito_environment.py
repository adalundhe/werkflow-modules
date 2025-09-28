from pydantic import BaseModel, StrictStr


class AppitoEnvironment(BaseModel):
    id: StrictStr | None = None
