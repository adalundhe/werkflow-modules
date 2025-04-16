import asyncio
import configparser
import functools
import pathlib
from concurrent.futures import ThreadPoolExecutor
from werkflow.modules.system import System
from werkflow_aws.models.parsing import AWSConfigRole


class AWSConfigParser:

    def __init__(self):
        self._loop: asyncio.AbstractEventLoop | None = None
        self._system = System()
        self._parser = configparser.ConfigParser()

        self._executor = ThreadPoolExecutor(
            max_workers=self._system.configuration.cores.physical
        )

    async def load(
        self,
        path: str,
        account: str,
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        path: pathlib.Path = await self._loop.run_in_executor(
            self._executor,
            functools.partial(
                pathlib.Path,
                path
            )
        )

        absolute_path = await self._loop.run_in_executor(
            self._executor,
            path.absolute
        )

        resolved_path = await self._loop.run_in_executor(
            self._executor,
            absolute_path.resolve
        )

        await self._loop.run_in_executor(
            self._executor,
            self._parser.read,
            str(resolved_path)
        )

        for section in self._parser.sections():
            pass

        matching_roles: dict[str, AWSConfigRole] = {}
        
        for section in self._parser.sections():
            section_line: str = section
            if section_line.startswith(f"profile {account}"):
                role_name = section_line.split()[1]  # Extract the role name from the section header

                role = AWSConfigRole(
                    role_name=role_name,
                    region=self._parser.get(section, 'region', fallback='N/A'),
                    source_profile=self._parser.get(section, 'source_profile', fallback='N/A'),
                    external_id=self._parser.get(section, 'external_id', fallback='N/A'),
                    role_arn=self._parser.get(section, 'role_arn', fallback='N/A'),
                )

                matching_roles[role_name] = role

        return matching_roles
    
    async def close(self):
        await self._system.close()

    def abort(self):
        self._system.abort()