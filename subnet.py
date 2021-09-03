from Ip import Ip

def getInitialAddress(ip):

	na = ''.join(ip.toBinary().split('.'))

	for bit in range(int(ip.getMask()), len(na)):
		na = na[ : bit] + "0" + na[bit + 1 : ]

	ans = ""
	for i in range(len(na)):
		if i % 8 == 0:
			ans += '.'
		ans += na[i]

	na = ans[1 : ]
	ans = ""
	for byte in na.split("."):
		ans += str(int(byte, 2)) + "."

	na = ans[ : -1]

	return Ip(na, ip.getMask())


with open("input.txt") as r:
	_input = r.readline().strip("\n").split('/')

	init_ip = Ip(_input[0], _input[1])
	print("IP =", init_ip)
	print(init_ip.toBinary())
	print()
	na = getInitialAddress(init_ip)

	print("N.A. =", na)
	print("B.A. =", na.getBroadcast())
	print("R.A. =", na.getRange())
	print()

	LANs = []
	for name, users in [line.strip("\n").split() for line in r.readlines()]:
		LANs.append((name, int(users)))

	LANs.sort(key = lambda lan : lan[1], reverse = True)

	for lan in LANs:
		name = lan[0]
		usersCount = lan[1]

		maskLength = 0
		for maskLength in range(0, 32):
			if usersCount + 2 <= (1 << maskLength):
				break
		maskLength = 32 - maskLength
		na.setMask(str(maskLength))

		print(name)
		print("N.A. =", na)
		print("B.A. =", na.getBroadcast())
		print("R.A. =", na.getRange())
		print()

		na = na.getBroadcast().nextIp()