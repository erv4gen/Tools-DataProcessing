import os , pickle

class Temp:
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