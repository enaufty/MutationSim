import random
base = ['A', 'T', 'G', 'C']
dna_length = int(input("DNA Length: "))
mutation = 7
uretilen = []
for i in range(dna_length):
    uretilen.append(random.choice(base))
print("".join(uretilen))
list(uretilen)
for i in range(mutation):
    orijinal_dizi = uretilen.copy()
    mutasyon_konumu = random.randint(0, dna_length-1)
    original_base = uretilen[mutasyon_konumu]
    new_base = original_base
    while new_base == original_base:
        new_base = random.choice(base)
        uretilen[mutasyon_konumu] = new_base
print("DNA with Mutation: " + "".join(uretilen))
for i in range(dna_length):
    if original_base != uretilen[i]:
        print("Position", i, ":", orijinal_dizi[i], "->", uretilen[i])
