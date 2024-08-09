from setuptools import setup, find_packages


# def readme():
#     with open('README.rst') as f:
#         return f.read()


setup(name='ngsCAT2',
      version='0.1',
      description='Next-Generation Sequencing Capture Assessment Tool 2',
      long_description='',
      classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9.7',
        'Topic :: Enrichment analysis',
      ],
      keywords='targeted sequencing  analysis ',
      url='https://github.com/alegarsan2/ngscat2',
      author='Alejandro García Sánchez',
      author_email='alegarsan2@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
        "certifi==2023.5.7",
        "chardet==4.0.0",
        "decorator==5.1.1",
        "idna==3.4",
        "ipython-genutils==0.2.0",
        "jsonschema==4.18.0",
        "jupyter-core==5.3.0",
        "nbformat==5.9.0",
        "numexpr==2.8.4",
        "numpy==1.24.3",
        "pandas==2.0.3",
        "plotly==5.15.0",
        "pysam==0.21.0",
        "python-dateutil==2.8.2",
        "pytz==2023.3",
        "requests==2.31.0",
        "retrying==1.3.4",
        "scipy==1.11.0",
        "six==1.16.0",
        "tables==3.9.2",
        "toolz==0.12.0",
        "traitlets==5.9.0",
        "urllib3==2.0.6",
        "xlwt==1.3.0",
    ],
      ],
      #test_suite='',
      #tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['ngscat2=ngscat2.main:main'],
      },
      include_package_data=True,
      zip_safe=False)
