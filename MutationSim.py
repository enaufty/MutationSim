import random
base = ['A', 'T', 'G', 'C']
dna_length = int(input('DNA length: '))
mutation = 10
uretilen = []
for i in range(dna_length):
    uretilen.append(random.choice(base))
print("".join(uretilen))
orijinal_dizi = uretilen.copy()
mutation_location = random.sample(range(dna_length), mutation)
for mutasyon_konumu in mutation_location:
    original_base = uretilen[mutasyon_konumu]
    new_base = original_base
    while new_base == original_base:
        new_base = random.choice(base)
    uretilen[mutasyon_konumu] = new_base
print("DNA with Mutation: " + "".join(uretilen))
for i in range(dna_length):
    note = " (changed)" if orijinal_dizi[i] != uretilen[i] else ""
    print(f"Position {i}: {orijinal_dizi[i]} -> {uretilen[i]}{note}")
