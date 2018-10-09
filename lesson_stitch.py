import yaml

# Change to the lesson file name below:
lesson_yaml = 'tables.en.yml';
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
					narrative = doc['components'][2]['content']
					outfile.write(narrative+'\n')
					if 'instructions' in doc['components'][2]:
						instructions = doc['components'][2]['instructions']
						outfile.write('instructions:\n')
						outfile.write(instructions+'\n')
					
