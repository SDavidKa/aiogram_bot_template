import httpx
from src.config import DJANGO_API_URL, DJANGO_API_TOKEN, BASE_URL

client = httpx.AsyncClient(
    base_url=f"{BASE_URL}{DJANGO_API_URL}",
    headers={"Authorization": f"Token {DJANGO_API_TOKEN}"},
    timeout=httpx.Timeout(10),
    limits=httpx.Limits(max_connections=100, max_keepalive_connections=10),
)