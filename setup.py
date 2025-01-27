import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="aquatic_coastal_analysis",                     
    version="0.0.0",                       
    author="Datsky",                     
    author_email="nickitadatsky@gmail.com",
    description="Software coplex complex for building geometrical images coastal systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nickitas/Aquatic-Coastal-Analysis",  
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # "requests>=2.0.0",
    ],
    entry_points={
        "console_scripts": [
            "my_program=my_program.src:main",
        ],
    },
)
