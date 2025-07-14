from pathlib import Path

path = Path('dist_out') / 'fakebin.txt'
path.touch()

path.write_text("Hello!")
