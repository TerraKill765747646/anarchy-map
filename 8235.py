import base64

maps = {
    'overworld': '2026-05-09_20.21.04_x-2512_z-2512.png',
    'nether': '2026-05-09_21.24.24_x-2512_z-2512.png'
}

encoded = {}
for dim, fname in maps.items():
    with open(fname, 'rb') as f:
        encoded[dim] = base64.b64encode(f.read()).decode()
    print(f'{dim} готов')

print('overworld length:', len(encoded['overworld']))
print('nether length:', len(encoded['nether']))