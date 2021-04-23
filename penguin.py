def peng(x):
	rest = x % 3
	eat = x - (rest)
	service = eat / 3

	if service + rest < 3:
		return service + rest
	else:
		eat += peng(service + rest)

	return eat

print(peng(20))
