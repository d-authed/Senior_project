import vt

from stix2 import Indicator
from stix2 import parse

client = vt.Client("d7927ed8b207357119e14557799c6d17c326a8bc1e317490c4dbc3db19c70f91")

file = client.get_object("/files/0284b8a1308bde25d8ea4c17c79f435b64825c80387693e5f985c10ee6bb68a3")
