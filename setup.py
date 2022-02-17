import setuptools

setuptools.setup(
    name="ldap-user-transfer",
    version="1.0.0",
    author="Furkan Kalkan",
    author_email="furkankalkan@mantis.com.tr",
    description="Script for transferring LDAP users from Postgresql database.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    platforms="all",
    url="https://github.com/mantis-software-company/ldap-user-transfer",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Internet",
        "Topic :: Software Development",
	    "Topic :: Software Development :: Testing",
        "System :: Systems Administration :: Authentication/Directory :: LDAP",
        "Intended Audience :: Developers",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Microsoft",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    install_requires=['python-ldap', 'PyYAML', 'psycopg2-binary'],
    python_requires=">3.6.*, <4",
    scripts=['src/ldap-user-transfer']
)