import setuptools

setuptools.setup(
	name = 'write_read',
	version = '1.0.0',
	description = 'Handling file read and write',
	packages = setuptools.find_packages('src'),
	package_dir = {'': 'src'}
	)