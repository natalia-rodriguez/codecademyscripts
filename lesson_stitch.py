import yaml

# Change to the lesson file name below:
lesson_yaml = 'what-is-vue.en.yml';
with open(lesson_yaml, 'r') as f:
	docs = yaml.load_all(f)
	for doc in docs:
		if 'exercises' in doc:
			exercises = doc['exercises']


with open('stitched_exercises.txt', 'w') as outfile:
	for exfile in exercises:
		with open('exercises/'+exfile+'.en.yml', 'r') as f:
			outfile.write(exfile+'\n')
			docs = yaml.load_all(f)
			for doc in docs:
				if 'components' in doc:
					outfile.write('Narrative:\n')
					for obj in doc['components']:
						if 'content' in obj:
							narrative = obj['content']
							outfile.write(narrative+'\n')
						if 'instructions' in obj:
							instructions = obj['instructions']
							outfile.write('instructions:\n')
							outfile.write(instructions+'\n')
					
