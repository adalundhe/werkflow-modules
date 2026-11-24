from __future__ import annotations

import asyncio
import functools
import pathlib
from concurrent.futures import ThreadPoolExecutor
from typing import Literal

from pydantic import BaseModel, Field, StrictBytes, StrictStr


FileReadMode = Literal['r', 'rb']


class File(BaseModel):
    name: StrictStr | None = None
    path: StrictStr | None = None
    content_disposition: StrictStr = "form-data"
    content_type: StrictStr = "application/octet-stream"
    encoding: StrictStr = "utf-8"
    headers: dict[StrictStr, StrictStr] = Field(default_factory=dict)
    data: StrictStr | StrictBytes | None = None
    mode: FileReadMode = 'r'

    def to_headers(self) -> dict[str, str]:
        disposition = self.content_disposition
        if ';' not in disposition:
            field_name = self.name or "file"
            filename = pathlib.Path(self.path).name if self.path else field_name
            disposition = f'{disposition}; name="{field_name}"; filename="{filename}"'

        headers: dict[str, str] = {
            "Content-Disposition": disposition,
            "Content-Type": self.content_type,
        }

        headers.update(self.headers)
        return headers

    def to_data(self) -> bytes | None:
        if isinstance(self.data, str):
            return self.data.encode(self.encoding)

        return self.data

    @classmethod
    async def upload(
        cls,
        path: str,
        name: str | None = None,
        content_type: str | None = None,
        mode: FileReadMode = 'r',
        executor: ThreadPoolExecutor | None = None,
    ) -> File:
        loop = asyncio.get_running_loop()

        owns_executor = executor is None
        if executor is None:
            executor = ThreadPoolExecutor(max_workers=1)

        file_path = pathlib.Path(path)

        if content_type is None:
            content_type = "application/octet-stream"

        try:
            full_path = await loop.run_in_executor(
                executor,
                file_path.absolute,
            )

            full_path = await loop.run_in_executor(
                executor,
                full_path.resolve,
            )

            if name is None:
                name = full_path.name

            data = await loop.run_in_executor(
                executor,
                functools.partial(
                    cls._upload,
                    str(full_path),
                    mode=mode,
                ),
            )

            return File(
                name=name,
                path=path,
                content_type=content_type,
                mode=mode,
                data=data,
            )

        finally:
            if owns_executor:
                executor.shutdown(wait=False)

    @classmethod
    def _upload(
        cls,
        path: str,
        mode: FileReadMode = 'r',
    ) -> str | bytes:
        with open(path, mode) as file:
            return file.read()
