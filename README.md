# CS361_Reading-Comprehensive-Assistant
It is a demo for Reading Comprehensive Assistant project

Currently this project includes a GUI that takes specific text input and produce corresponding graph to show the user what this software is meant to achieve. 

The demo is accomplished by writing text into communication file and reading in generated image path.

The text_comm.py micro-service will write received information into the image-service.txt, and img.py micro-service will read the same file and write path of generated graph to the file. 

In the furture plan, these two micro-service will be replaced by trained NLP model that returns the true generated graph, and the GUI will be modified with better design.
