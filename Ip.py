class Ip:

	def __init__(self, ip, mask):
		self.ip = ip
		self.mask = mask

	def __str__(self):
		return self.ip + "/" + self.mask

	def getBroadcast(self):
		broadcast = ''.join(self.toBinary().split('.'))
		for bit in range(int(self.mask), len(broadcast)):
			broadcast = broadcast[ : bit] + "1" + broadcast[bit + 1 : ]

		res = ""
		for i in range(4):
			res += str(int(broadcast[8 * i : 8 * (i + 1) ], 2)) + "."
		res = res[ : -1]

		return Ip(res, self.mask)

	def getRange(self):
		na = self.nextIp()
		broadcast = self.getBroadcast().prevIp()

		return na.ip + "-" + broadcast.ip + "/" + str(self.mask)

	def setMask(self, mask):
		self.mask = mask

	def getMask(self):
		return self.mask

	def nextIp(self):
		bytes = [int(x) for x in self.ip.split(".")]
		toAdd = 1
		for i in range(3, -1, -1):
			bytes[i] += toAdd
			toAdd = bytes[i] // 256
			bytes[i] %= 256

		return Ip('.'.join([str(x) for x in bytes]), self.mask)

	def prevIp(self):
		bytes = [int(x) for x in self.ip.split(".")]
		toSubtract = 1
		for i in range(3, -1, -1):
			if bytes[i] == 0:
				bytes[i] = 255
				toSubtract = 1
			else:
				bytes[i] -= toSubtract
				toSubtract = 0

		return Ip('.'.join([str(x) for x in bytes]), self.mask)

	def toBinary(self):
		ans = ""
		for byte in self.ip.split("."):
			ans += "{0:08b}".format(int(byte)) + "."
		ans = ans[ : -1]
		return ans