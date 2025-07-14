import sys
from pathlib import Path

path = Path('dist_out') / f'fakebin-{sys.platform}.txt'
path.touch()

path.write_text("Hello!")
