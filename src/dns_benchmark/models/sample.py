from dataclasses import dataclass

@dataclass
class Sample:
    resolver: str
    test_type: str
    latency: float | None
    success: bool