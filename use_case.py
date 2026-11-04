import re
import json
from pydantic import BaseModel

from agent import build_agent
from agent_tools import get_all_tools


def _text(content) -> str:
    if isinstance(content, str):
        return content
    return "".join(b.get("text", "") for b in content if isinstance(b, dict))

class Usecase:
    def __init__(self, 
                 name:str, 
                 model: str, 
                 system_prompt: str, 
                 base_model: BaseModel):
        self.name = name,
        self.model = model
        self.system_prompt = system_prompt
        self.base_model = base_model
        self.agent = None

    def build_agent(self):
        self.agent = build_agent(self.system_prompt, 
                                 model=self.model,
                                 tools=get_all_tools(),
                                 skill_folder_path="/skills/org-skills/")

    def run(self, user_prompt: str) -> BaseModel:
        print("Running use case:", self.name)
        result = build_agent(self.system_prompt, model=self.model).invoke(
            {"messages": [{"role": "user", "content": user_prompt}]}
        )
        raw = _text(result["messages"][-1].content)
        match = re.search(r"\{.*\}", raw, re.DOTALL)
        if not match:
            raise ValueError(f"No JSON object in agent output:\n{raw}")
        return self.base_model.model_validate(json.loads(match.group(0)))
    