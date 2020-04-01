import unittest;
import sort;

class TestSum(unittest.TestCase):
	def setUp(self):
		self.results = sort.sort_text();

		self.expected = ['\n',' Kha\n', ' Asby\n', ' Bain\n', ' Dean\n', ' Fife\n', ' Wile\n', ' Baker\n', ' Ellis\n', ' Evans\n', ' Foley\n', ' Glock\n', ' Graff\n', 
		' Heigl\n', ' Lundy\n', ' McVey\n', ' Nylon\n', ' Peery\n', ' Reyes\n', ' White\n', ' Adkins\n', ' Broome\n', ' Hickey\n', ' Laymon\n', ' Rogers\n', ' Tanton\n',
		' Taylor\n', ' Byfield\n', ' Dulaney\n', ' Hagberg\n', ' Hillman\n', ' McCrave\n', ' Michael\n', ' Padgett\n', ' Routson\n', ' Starkey\n', ' Stegman\n', 
		' Bostwick\n', ' Cachedon\n', ' Giddings\n', ' Guenther\n', ' Hatfield\n', ' Kalivoda\n', ' Kirkland\n',' Phillips\n', ' Reynolds\n', ' Sullivan\n', ' Williams\n',
		' Clevenger\n', ' Fitzjerrell\n', ' Hendrickson\n'];

	def test_Sort(self):
		self.assertListEqual(self.results,self.expected);

if __name__ == '__main__':
    unittest.main()
