import random
import asyncio
from typing import List
from dns_benchmark.models.sample import Sample
from dns_benchmark.models.resolver import Resolver
from dns_benchmark.engine.client import dns_query

CACHED_DOMAINS = ["google.com", "youtube.com", "amazon.com"]
UNCACHED_BASE = ["google.com", "cloudflare.com"]
DOTCOM_DOMAINS = ["com"]

SAMPLES_PER_TYPE = 5  # aumenta robustez


async def run_resolver(resolver: Resolver) -> List[Sample]:
    tasks = []

    # Cached
    for _ in range(SAMPLES_PER_TYPE):
        for d in CACHED_DOMAINS:
            tasks.append(run_single(resolver, "cached", d))

    # Uncached
    for _ in range(SAMPLES_PER_TYPE):
        for d in UNCACHED_BASE:
            rand = f"bench{random.randint(0,999999)}.{d}"
            tasks.append(run_single(resolver, "uncached", rand))

    # Dotcom
    for _ in range(SAMPLES_PER_TYPE):
        for d in DOTCOM_DOMAINS:
            tasks.append(run_single(resolver, "dotcom", d, qtype=2))

    return await asyncio.gather(*tasks)


async def run_single(resolver, test_type, domain, qtype=1):
    latency = await dns_query(resolver.ip, domain)
    return Sample(resolver.ip, test_type, latency, latency is not None)