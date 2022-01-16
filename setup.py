from distutils.core import setup


def readme():
    """Import the README.md Markdown file and try to convert it to RST format."""
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        with open('README.md') as readme_file:
            return readme_file.read()


setup(
    name='book_recommender',
    version='0.1',
    description='A book recommender based on goodreads dataset',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    # Substitute <github_account> with the name of your GitHub account
    url='',
    author='Jin Zhang',  # Substitute your name
    author_email='jinzh001@gmail.com',  # Substitute your email
    license='MIT',
    packages=['book_recommender'],
    install_requires=['pypandoc>=1.4']
)
