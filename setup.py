"""Setup Package Configuration
"""
from setuptools import setup, find_packages


setup(
    name="treescriptify-text",
    version="0.3",
    description="Create TreeScript from a Text file that contains tree-like file information.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="DK96-OS",
    url="https://github.com/DK96-OS/treescriptify-text",
    project_urls={
        "Issues": "https://github.com/DK96-OS/treescriptify-text/issues",
        "Source Code": "https://github.com/DK96-OS/treescriptify-text"
    },
    license="GPLv3",
    packages=find_packages(exclude=['test']),
    entry_points={
        'console_scripts': [
            'treescriptify_text=treescriptify_text.__main__:main',
            'treescriptify-text=treescriptify_text.__main__:main',
        ],
    },
    python_requires='>=3.10',
    classifiers=[
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
)
