# BTech Project : Penetration Testing of HTTP/3.0 Servers

Please refer this [link](https://docs.google.com/spreadsheets/d/1JcexNmwQSTxIEzCDZede9PI-nHgD3X-RktHXfKvXJeI/edit?usp=sharing) for readings of Handshake Time & Packet RX Time observed for different servers while testing.

Experiment description :-

* Experiment 1 : Changing Version to 0 (Version negotation)
* Experiment 2 : Changing Version to a positive value
* Experiment 3 : Changing fixed bit in the public flag
* Experiment 4 : Changing packet number length
* Experiment 5 : Buffer overflow

> For experiments related to each server, there is a directory associated with it. It consists of script for flooding subdivided by the type of experiment (Types of experiments are mentioned above). Screenshot of the reading observed during experiment is also present in the same directory.

> To perform the experiment run the script by ```python script.py``` from the directory concerned.

Group Members:

* Shaan Kumar (19074015)
* Naresh Kumar (19075047)
* Nikita (19075048)