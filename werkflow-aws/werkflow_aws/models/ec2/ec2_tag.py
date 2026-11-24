from pydantic import BaseModel, StrictStr


class EC2Tag(BaseModel):
    Key: StrictStr
    Value: StrictStr | None = None
