build: clean
	mkdir -p dist/build
	zip -r dist/build/ocio_file_input_addon.zip ocio_file_input_addon

clean:
	find . -name \*.pyc -delete
	find . -name __pycache__ -delete

test:
	python3 -m unittest discover

coverage:
	coverage run -m unittest discover
	coverage report -m
