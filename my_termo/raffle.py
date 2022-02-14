import json
import random
from datetime import datetime
from pathlib import Path


def raffle_word() -> str:
    """This function raffle one word of the words set."""
    with open(Path(__file__).parent / 'words.json') as f:
        random.seed(datetime.today().date().toordinal())
        return random.choice(json.load(f))
