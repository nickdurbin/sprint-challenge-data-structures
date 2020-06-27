from doubly_linked_list import DoublyLinkedList

class RingBuffer:
	def __init__(self, capacity):
		self.capacity = capacity
		self.current = None
		self.storage = DoublyLinkedList()

	def append(self, item):
		# check the current storage
		# if the storage is less than current capacity
		# make the last item the current item
		if self.storage.length < self.capacity:
			self.storage.add_to_tail(item)
			self.current = self.storage.tail
		# if the current stoage is equal to the capacity
		# set the current value to the item
		if self.storage.length == self.capacity:
			self.current.value = item
			# if the current node is the tail
			# set the value also to head
			# as they would be one and the same
			if self.current is self.storage.tail:
				self.current = self.storage.head
			# if not then set it to the enxt node
			else:
				self.current = self.current.next
					
	def get(self):
		# create a buffer list
		buffer = []
		# set the current node to the head
		current_node = self.storage.head
		# while the current node is not None
		# or if a list exists basically
		while current_node is not None:
			# check to make sure the current v is aluenot none
			if current_node.value is not None:
				# add the value to the buffer list
				buffer.append(current_node.value)
			# point it tot he next node
			current_node = current_node.next
	
		return buffer