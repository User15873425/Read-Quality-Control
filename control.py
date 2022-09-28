import gzip

ATGCs, repeats_and_Ns = [], []
for i in range(3):
    with gzip.open(input()) as data:
        ATGCs += [data.read().decode('utf-8').splitlines()[1::4]]
        repeats_and_Ns.append((len(ATGCs[i]) - len(set(ATGCs[i])), *[sum(1 for seq in ATGCs[i] if 'N' in seq)]))
best = (lambda a: ATGCs[idx])(idx := repeats_and_Ns.index(min(repeats_and_Ns)))
print(f'Reads in the file = {len(best)}', 'Reads sequence average length = {}\n'.format(
    round(sum(len(seq) for seq in best) / len(best))), f'Repeats = {repeats_and_Ns[idx][0]}',
    f'Reads with Ns = {repeats_and_Ns[idx][1]}\n', 'GC content average = {}%'.format(
    (lambda x: round(sum(x) / len(x), 2))([sum(sym in 'GC' for sym in seq) / len(seq) * 100 for seq in best])),
    f"Ns per read sequence = {round(sum(seq.count('N') / len(seq) * 100 for seq in best) / len(best), 2)}%", sep='\n')
