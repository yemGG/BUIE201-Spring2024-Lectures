class School:
	def __init__(self, name) -> None:
		self._name = name

	def print(self):
		pass

class University(School):
	def __init__(self, name) -> None:
		super.__init__(name)

	def print(self):
		str = "(" + self._name + ", University)"
		return str
	
class HighSchool(School):
	def __init__(self, name, language) -> None:
		super.__init__(name)
		self._language = language

	def print(self):
		str = "(" + self._name + ", " + self._language + ", HighSchool)"
		return str

class City:
	def __init__(self, name) -> None:
		self._name = name
		self._schools = []

	def add_school(self, s : School):
		self._schools.append(s)
		return s

	def print (self):
		str = self._name + " => "
		for s in self._schools:
			str += s.print() + ", "
		return str

class Map:
	def __init__(self) -> None:
		self._cities = []

	def add_city(self, c : City):
		self._cities.append(c)
		return c

	def print(self):
		str = ""
		for c in self._cities:
			if str is not "":
				str += "; "
			str += c.print()
		return str





# Add your code before this line. Do not change the code below this line.

def Run():
	m = Map()
	C1 = m.add_city(City("Istanbul"))
	C2 = m.add_city(City("Konya"))

	C1.add_school(University("BU"))
	C2.add_school(University("Selcuk"))
	C1.add_school(University("ITU"))
	C1.add_school(HighSchool("DSI", "German"))
	C1.add_school(HighSchool("GS", "French"))
	C2.add_school(HighSchool("KAL", "English"))

	return m.print()


print (Run())