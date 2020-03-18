import os , pickle

class Temp:
	'''
	class version of the temp
	'''
	path_to_temp = os.path.expanduser('~')
	ext = '.pickl'
	@classmethod
	def set_path(Temp,path):
		Temp.path_to_temp = path
	
	@classmethod
	def save_obj(Temp,obj,name):
		if name is None:
			name = str(id(obj))
		with open(Temp.path_to_temp+name+Temp.ext , 'wb') as f:
			pickle.dump(obj,f)
		print('Object <'+str(id(obj))+'> saved to:',Temp.path_to_temp)

	@classmethod
	def load_obj(Temp,fild_id):
		with open(Temp.path_to_temp+fild_id+Temp.ext , 'rb') as f:
			obj = pickle.load(f)
		print('Object <'+str(fild_id)+'> loaded from:',Temp.path_to_temp)
		return obj



class Tempdir:
	'''
	object version of the temp dir
	'''
	def __init__(self,path=None):
		self.ext = '.pickl'	
		if not path:
			self.path_to_temp = os.path.expanduser('~')
		else:
			self.path_to_temp = path
		
	def save_obj(self,obj,name):
		if name is None:
			name = str(id(obj))
		with open(self.path_to_temp+name+self.ext , 'wb') as f:
			pickle.dump(obj,f)
		print('Object <'+str(id(obj))+'> saved to:',self.path_to_temp)

	def load_obj(self,fild_id):
		with open(self.path_to_temp+fild_id+Temp.ext , 'rb') as f:
			obj = pickle.load(f)
		print('Object <'+str(fild_id)+'> loaded from:',self.path_to_temp)
		return obj