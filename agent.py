"""Company research agent: organisation name + URL in, three-field profile out.

Usage:
    python agent.py "Acme Learning" https://www.acme-learning.com

Env vars: ANTHROPIC_API_KEY, TAVILY_API_KEY. Optional: MODEL (default below).
"""
import argparse
import json
import os
import re
from pathlib import Path

from deepagents import FilesystemPermission, create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend
from langchain.tools import tool
from pydantic import BaseModel
from tavily import TavilyClient

from dotenv import load_dotenv
load_dotenv()

ROOT = Path(__file__).parent
MODEL = os.getenv("MODEL", "anthropic:claude-haiku-5-5")
_tavily = TavilyClient()  # reads TAVILY_API_KEY

SYSTEM_PROMPT = (
    "You research organisations using web data only. Before answering, read and follow "
    "the `company-research` skill, then the `company-profile-output` skill for the final answer."
)


class CompanyProfile(BaseModel):
    description: str
    employee_strength: str
    main_sector: str


@tool
def web_search(query: str, max_results: int = 5) -> str:
    """Search the web. Returns title, URL and a content snippet for each result."""
    res = _tavily.search(query, max_results=max_results)
    return "\n\n".join(f"{r['title']}\n{r['url']}\n{r['content']}" for r in res["results"])


@tool
def fetch_url(url: str) -> str:
    """Fetch a web page and return its text content (truncated to 8000 characters)."""
    res = _tavily.extract(urls=[url])
    if not res["results"]:
        return f"Could not fetch {url}"
    return res["results"][0]["raw_content"][:8000]


def build_agent():
    backend = FilesystemBackend(root_dir=ROOT, virtual_mode=True)
    return create_deep_agent(
        model=MODEL,
        backend=backend,
        tools=[web_search, fetch_url],
        skills=["/skills/"],
        system_prompt=SYSTEM_PROMPT,
        # Agent may read skills but never modify them
        permissions=[FilesystemPermission(operations=["write"], paths=["/skills/**"], mode="deny")],
    )


def _text(content) -> str:
    if isinstance(content, str):
        return content
    return "".join(b.get("text", "") for b in content if isinstance(b, dict))


def research(name: str, url: str) -> CompanyProfile:
    result = build_agent().invoke(
        {"messages": [{"role": "user", "content": f"Organisation: {name}\nWebsite: {url}"}]}
    )
    raw = _text(result["messages"][-1].content)
    match = re.search(r"\{.*\}", raw, re.DOTALL)
    if not match:
        raise ValueError(f"No JSON object in agent output:\n{raw}")
    return CompanyProfile.model_validate(json.loads(match.group(0)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Three-field company profile from web research")
    parser.add_argument("name", help="Organisation name")
    parser.add_argument("url", help="Organisation website URL")
    args = parser.parse_args()
    print(research(args.name, args.url).model_dump_json(indent=2))
