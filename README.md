# README

Questo codice contiene una semplice calcolatrice che esegue l'operazione di:
- somma tra due numeri
- sottrazione tra due numeri

Include anche test unitari per verificare il corretto funzionamento della funzione di somma.

## Requisiti

- Aver installato UV da https://github.com/astral-sh/uv

- Creare un ambiente virtuale
    - python3 -m venv .venv

    - rm -rf .venv
	- uv venv

- Attivare l'ambiente virtuale
    - source .venv/bin/activate  (Linux/Mac)
    - .venv\Scripts\activate    (Windows)    

- verifica che l'interprete sia quello gisuto
    - which python3 ( Linux/Mac)
    - where python   (Windows)

- Installare le dipendenze
    - pip install -r requirements.txt

    - uv pip compile requirements.in -o requirements.txt
    - uv pip install -r requirements.txt

## Esecuzione normale

python3 calcolatrice.py

## Esecuzione dei test

pytest -v


## Github upload

- git init
- git add .
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/sammmp123
- git push -u origin main

## Docker build

- docker build - f Dockerfile -t devops-calcolatrice-main:local . (compila file docker file)
- docker run --rm -it devops-calcolatrice-main:local   (fa eseguire in modo interattivo dell'immagine che hai appena creato elimina automaticamente il container che crea)

## Docker Hub upload