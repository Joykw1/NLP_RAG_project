# Natural Language Processing: RAG project

This is the repository for the NLP project on Retrieval Augmented Generation. The team includes:
- Elizaveta Ershova
- Flor Alberts
- Joy Kwant
- Theo Krijgsheld

The project is split up in different Python notebooks found in the ``Code`` folder. The notebooks are created in Goole Colab and include a button to automatically open them in Google Colab. It is easiest to run them there.

## Pipeline

The files ``Multipassage_retrieval.ipynb`` and ``Language_detection.ipynb`` work together in a pipeline in the sense that ``Language_detection.ipynb`` requires the output of ``Multipassage_retrieval.ipynb`` as an input. Therefore, you should be sure to run ``Multipassage_retrieval.ipynb`` before running ``Language_detection.ipynb`` and you chould ensure the output of ``Multipassage_retrieval.ipynb`` is stored in the right place.

## Install the dependencies 

If you do not want to use Google Colab to run the code, you can install the dependencies found in ``requirements.txt``.

``requirements.txt`` includes a list of all the packages used in our code. To install them run 
```
pip install -r requirements.txt
```

