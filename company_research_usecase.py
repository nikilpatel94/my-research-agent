from argparse import ArgumentParser
from use_case import Usecase

from pydantic import BaseModel

class CompanyProfile(BaseModel):
    description: str
    employee_strength: str
    main_sector: str


SYSTEM_PROMPT = (
    "You research organisations using web data only. Before answering, read and follow "
    "the `company-research` skill, then the `company-profile-output` skill for the final answer."
)

NAME = "Company Research"

def research(name: str, url: str, validation_base_model: BaseModel) -> CompanyProfile:
    usecase = Usecase(name = NAME, 
                      model="anthropic:claude-haiku-5-5", 
                      system_prompt=SYSTEM_PROMPT, 
                      base_model=validation_base_model)
    user_prompt = f"Organisation: {name}\nWebsite: {url}"
    return usecase.run(user_prompt)



if __name__ == "__main__":
    parser = ArgumentParser(description="Three-field company profile from web research")
    parser.add_argument("name", help="Organisation name")
    parser.add_argument("url", help="Organisation website URL")
    args = parser.parse_args()
    print(research(args.name, args.url, validation_base_model=CompanyProfile).model_dump_json(indent=2))

