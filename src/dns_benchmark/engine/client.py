import asyncio
import random
import struct
import time


def encode_qname(name: str) -> bytes:
    parts = name.split('.')
    res = b''
    for part in parts:
        res += bytes([len(part)]) + part.encode()
    return res + b'\x00'


def build_query(name: str, qtype: int = 1):
    qid = random.randint(0, 65535)
    header = struct.pack("!HHHHHH", qid, 0x0100, 1, 0, 0, 0)
    question = encode_qname(name) + struct.pack("!HH", qtype, 1)
    return qid, header + question


async def dns_query(server: str, name: str, qtype=1, timeout=1.5, retries=1):
    for attempt in range(retries + 1):
        loop = asyncio.get_running_loop()
        future = loop.create_future()

        class Proto(asyncio.DatagramProtocol):
            def datagram_received(self, data, addr):
                if not future.done():
                    future.set_result(data)

        transport, _ = await loop.create_datagram_endpoint(
            lambda: Proto(), remote_addr=(server, 53)
        )

        try:
            qid, payload = build_query(name, qtype)
            start = time.perf_counter()
            transport.sendto(payload)
            data = await asyncio.wait_for(future, timeout)
            latency = time.perf_counter() - start

            if struct.unpack("!H", data[:2])[0] != qid:
                raise Exception("Invalid response")

            return latency

        except Exception:
            if attempt == retries:
                return None

        finally:
            transport.close()