import base64, os
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, 'art.b85'), 'r', encoding='ascii') as f:
    data = base64.b85decode(''.join(f.read().split()))
out = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, 'entry.png'), 'wb') as f:
    f.write(data)
