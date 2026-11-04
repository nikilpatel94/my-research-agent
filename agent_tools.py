from langchain.tools import tool
from tavily import TavilyClient

@tool
def web_search(query: str, max_results: int = 5) -> str:
    """Search the web. Returns title, URL and a content snippet for each result."""
    _tavily = TavilyClient()  # reads TAVILY_API_KEY
    res = _tavily.search(query, max_results=max_results)
    return "\n\n".join(f"{r['title']}\n{r['url']}\n{r['content']}" for r in res["results"])


@tool
def fetch_url(url: str) -> str:
    """Fetch a web page and return its text content (truncated to 8000 characters)."""
    _tavily = TavilyClient()  # reads TAVILY_API_KEY
    res = _tavily.extract(urls=[url])
    if not res["results"]:
        return f"Could not fetch {url}"
    return res["results"][0]["raw_content"][:8000]

def get_all_tools()->list[tool]:
    return [web_search, fetch_url]