from pydantic import BaseModel, StrictStr


class DimensionValueAttribute(BaseModel):
    Value: StrictStr
    Attributes: dict[StrictStr, StrictStr]

    def dump(self):
        return self.model_dump()