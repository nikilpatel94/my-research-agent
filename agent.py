
import os
from pathlib import Path

from deepagents import FilesystemPermission, create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend
from dotenv import load_dotenv

from agent_tools import get_all_tools

load_dotenv()

ROOT = Path(__file__).parent
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "anthropic:claude-haiku-5-5")
DEFAULT_TOOLS = get_all_tools()


def build_agent(system_prompt: str,
                model: str=DEFAULT_MODEL,
                tools:list=DEFAULT_TOOLS, 
                skill_folder_path:str="/skills/"):
    backend = FilesystemBackend(root_dir=ROOT, virtual_mode=True)
    return create_deep_agent(
        model=model,
        backend=backend,
        tools=tools,
        skills=[skill_folder_path],
        system_prompt=system_prompt,
        # may read skills but never modify them
        permissions=[FilesystemPermission(operations=["write"], paths=[f"{skill_folder_path}**"], mode="deny")],
    )

