from collections.abc import Sequence
from typing import ClassVar, Self


class Module:
    module_enabled: ClassVar[bool] = True
    dependencies: ClassVar[Sequence[str]] = ()

    def __init__(self) -> None:
        pass

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        await self.close()

    async def close(self) -> None:
        pass

    def abort(self) -> None:
        pass
