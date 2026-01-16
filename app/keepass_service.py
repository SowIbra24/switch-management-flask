import os 
import re
from pykeepass import PyKeePass # pyright: ignore[reportMissingImports]
from dotenv import load_dotenv # pyright: ignore[reportMissingImports]

load_dotenv()

KEEPASS_DB_PATH = os.getenv("KEEPASS_DB_PATH")
KEEPASS_KEY_PATH = os.getenv("KEEPASS_KEY_PATH")
SITES = os.getenv("SITES","").split(',')
SWITCH_REGEX = os.getenv("SWITCH_REGEX")

for key, value in os.environ.items():
    print(f"{key}={value}")

def open_database():
    return PyKeePass(
        KEEPASS_DB_PATH,
        keyfile=KEEPASS_KEY_PATH
    )


def get_all_switches():
    kp = open_database()
    switches = {}

    for site in SITES:
         # récupère **tous les groupes sous "Réseau"**
        group = kp.find_groups(path=["Réseau", site], first=True)
        if not group:
            continue

        switches[site] = []

        for entry in group.entries:
            if re.match(SWITCH_REGEX, entry.title):
                switches[site].append({
                    "title": entry.title,
                    "username": entry.username,
                    "password": entry.password,
                    "url": entry.url
                })

    return switches


def get_switch_by_name(name):
    kp = open_database()
    return kp.find_entries(title=name, first=True)
