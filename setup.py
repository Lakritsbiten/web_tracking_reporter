import setuptools

setuptools.setup(
    name='tracking_reporter',
    version='0.0.10',
    author='Stefan Solender',
    author_email='stefan.solender@gmail.com',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Developers',
    ],
    python_requires='>=3.7',
    install_requires=[
        'setuptools',
        'flask',
        'dateparser',
        'pandas',
    ],
    include_package_data=True,
    zip_safe=False,
)
