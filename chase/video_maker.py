

import wikipedia



def wikivideo(query='New York'):
	ny = wikipedia.page(query)
	print ny.content

def download_images():
	pass


if __name__ == '__main__':
	wikivideo()