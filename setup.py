from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

setup(
	name="hawc_crm",
	version="1.0.0",
	description="CRM app for HAWC",
	author="ss-sevesh",
	author_email="ss-sevesh@github.local",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
