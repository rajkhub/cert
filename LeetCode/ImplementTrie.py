class Trie(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.s = set()

	def insert(self, word):
		"""
		Inserts a word into the trie.
		"""
		self.s.add(word)

	def search(self, word):
		"""
		Returns if the word is in the trie.
		"""
		return word in self.s

	def startsWith(self, prefix):
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		"""
		for i in self.s:
			if i.startswith(prefix):
				return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
