from enum import Enum
from pydantic import BaseModel, constr

import outlines
from openai import OpenAI
from outlines.models.openai import OpenAIConfig
import torch

import os 

import dotenv

dotenv.load_dotenv()

class Weapon(str, Enum):
    sword = "sword"
    axe = "axe"
    mace = "mace"
    spear = "spear"
    bow = "bow"
    crossbow = "crossbow"


class Armor(str, Enum):
    leather = "leather"
    chainmail = "chainmail"
    plate = "plate"


class Character(BaseModel):
    name: constr(max_length=10)
    age: int
    armor: Armor
    weapon: Weapon
    strength: int


# use ENV variables
MODEL = "akjindal53244/Llama-3.1-Storm-8B"


OPENAI_BASE_URL = os.getenv("VLLM_API_URL")
OPENAI_API_KEY = os.getenv("VLLM_API_KEY") 

client = OpenAI(
        api_key=OPENAI_API_KEY, 
        base_url=OPENAI_BASE_URL,
    )

config = OpenAIConfig(MODEL)
model = outlines.models.openai(client,config)

# Construct structured sequence generator
generator = outlines.generate.json(model, Character)

# Draw a sample
seed = 789001

character = generator("Give me a character description", seed=seed)

print(repr(character))
# Character(name='Anderson', age=28, armor=<Armor.chainmail: 'chainmail'>, weapon=<Weapon.sword: 'sword'>, strength=8)

character = generator("Give me an interesting character description", rng=rng)

print(repr(character))
# Character(name='Vivian Thr', age=44, armor=<Armor.plate: 'plate'>, weapon=<Weapon.crossbow: 'crossbow'>, strength=125)
