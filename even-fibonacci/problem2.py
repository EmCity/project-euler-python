seq = [1,2]
while seq[-1] <= 4000000:
	seq.append(seq[-1]+seq[-2])
newseq = [i for i in seq if i%2 == 0]
print(sum(newseq))