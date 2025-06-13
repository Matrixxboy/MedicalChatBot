from setuptools import setup, find_packages

setup(
    name='medbot',
    author="Matrixxboy",
    author_email="matrix.utsav.lankapati@gmail.com",
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn',
        'langchain',
        'python-dotenv',
        'groq',
        'tqdm',
        'chromadb',
        'faiss-cpu'
    ],
)
