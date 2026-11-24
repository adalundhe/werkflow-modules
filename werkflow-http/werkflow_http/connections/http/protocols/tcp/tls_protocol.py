from weakref import ref

from werkflow_http.connections.http.protocols.shared import Reader
from .protocol import TCPProtocol


class TLSProtocol(TCPProtocol):

    def upgrade_reader(self, reader: Reader) -> None:
        if self._stream_reader is not None:
            self._stream_reader.set_exception(
                Exception('upgraded connection to TLS, this reader is obsolete now.')
            )

        self._stream_reader_wr = ref(reader)
        self._source_traceback = reader._source_traceback
