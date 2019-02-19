#!/bin/bash
python src/manage.py migrate
python src/manage.py runserver 0:80
echo Running Django on the local host at http://localhost:9000
