import time
class Node(object):
	def __init__(self, data):
		self.parent = None
		self.data = data
		self.child = []
		self.childData = []
		self.state = True
	def add_child(self, obj):
		obj.parent = self
		self.child.append(obj)
		self.childData.append(obj.data)
	def get_level(self):
		level = 0 
		p = self.parent
		while p :
			p = p.parent
			level += 1
		return level
	def child_alive(self):
		#print([x.data for x in self.child],[x.state for x in self.child])
		return [x for x in self.child if x.state==True]
				
	def print_tree(self,state=False,show_dead=True):
		if not show_dead and not self.state:
			return
		print('  '*self.get_level() + '|--', end = '')
		if not state:print(f"{self.data}")
		elif state:print(f"{self.data}:[{self.state}]")
		if self.child:
			for each in self.child:
				each.print_tree(state=state,show_dead=show_dead)

	def print_parentage(self):
		print(self.data,end="")
		if self.parent:
			print("-->",end="")
			self.parent.print_parentage()
		else:
			print()
def timer(func):
	def decorated_func(*args,**kwargs):
		start_time = time.time()
		a = func(*args,**kwargs)
		print("--- %s seconds ---" % (time.time() - start_time))
		return a
	return decorated_func

def child(Parent,child):
	node = Node(child)
	Parent.add_child(node)
	return node
def treeify(listA):
	root = Node("Start")
	useless_var = None
	for i in listA:
		for j in range(len(i)):
			if j == 0 and (i[j] not in root.childData):
				useless_var = child(root,i[j])
			elif j == 0:
				#useless_var = [x for x in root.child if x.data == i[j]][0]
				useless_var = root.child[root.childData.index(i[j])]
			elif i[j] not in useless_var.childData:
				useless_var = child(useless_var,i[j])
			else:
				useless_var = useless_var.child[useless_var.childData.index(i[j])]
	return root
def bottomView(root):
	listb = []
	for x in root.child:
		posic = [x]
		for _ in range(10):
			posic2 = posic
			posic = []
			for j in posic2:
				if j.child == []:
					listb += [j]
					continue
				else:
					posic += j.child
	return listb

def kill_node(Node):
	Node.state = False
	for x in Node.child:
		kill_node(x)
def kill_sibling(Node):
	for x in Node.parent.child:
		if x != Node:
			kill_node(x)
def print_sepcific(Dot):
	level = Dot.get_level()
	parents = []
	temp = Dot
	for i in range(level):
		temp = temp.parent
		parents += [temp]
	parents = reversed(parents)
	for x in parents:
		print('  '*x.get_level() + '|--', end = '')
		print(f"{x.data}")
	Dot.print_tree()
def main():
	listA =	[["X","O","X"],["X","O","O"],["O","O","O"],["O","X","X"],["O","O","X"],["O","X","O"]]
	tree = treeify(listA)
	tree.print_tree(state=True)
	view = bottomView(tree)
	print(tree.child_alive())
	print(tree.child[tree.childData.index("O")].get_level())
	kill_sibling(tree.child[tree.childData.index("O")])
	print("<>")
	tree.print_tree(state=True)
	print("<>")
	tree.print_tree(state=True,show_dead=False)
	view[3].print_parentage()
	print_sepcific(tree.child[tree.childData.index("X")])
if __name__ == "__main__":
	main()