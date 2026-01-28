from typing import Dict, Optional


# Built-in stitch abbreviation dictionary
# This is intentionally minimal for MVP
ABBREVIATIONS: Dict[str, Dict[str, Dict[str, str]]] = {
    "knit": {
        "k": {
            "name": "Knit",
            "description": "Insert needle into the stitch from front to back and pull a new loop through."
        },
        "p": {
            "name": "Purl",
            "description": "Insert needle into the stitch from back to front and pull a new loop through."
        },
        "yo": {
            "name": "Yarn Over",
            "description": "Wrap the yarn over the needle to create a new stitch."
        },
        "k2tog": {
            "name": "Knit Two Together",
            "description": "Knit two stitches together as one (right-leaning decrease)."
        },
        "ssk": {
            "name": "Slip Slip Knit",
            "description": "Slip two stitches knitwise, then knit them together (left-leaning decrease)."
        },
    },
    "crochet": {
        "ch": {
            "name": "Chain",
            "description": "Create a chain stitch by pulling yarn through the loop on the hook."
        },
        "sc": {
            "name": "Single Crochet",
            "description": "Insert hook, yarn over, pull up a loop, yarn over and pull through both loops."
        },
        "hdc": {
            "name": "Half Double Crochet",
            "description": "Yarn over, insert hook, pull up a loop, yarn over and pull through all loops."
        },
        "dc": {
            "name": "Double Crochet",
            "description": "Yarn over, insert hook, pull up a loop, yarn over pull through two loops twice."
        },
        "sl st": {
            "name": "Slip Stitch",
            "description": "Insert hook, yarn over, pull yarn through stitch and loop on hook."
        },
    }
}


def lookup(craft_type: str, abbrev: str) -> Optional[Dict[str, str]]:
    """
    Look up a stitch abbreviation.

    Parameters
    ----------
    craft_type : str
        Either "knit" or "crochet"
    abbrev : str
        Abbreviation to look up (e.g. "k2tog", "sc")

    Returns
    -------
    dict or None
        Dictionary with name and description if found, otherwise None
    """
    craft = craft_type.lower().strip()
    key = abbrev.lower().strip()

    return ABBREVIATIONS.get(craft, {}).get(key)

