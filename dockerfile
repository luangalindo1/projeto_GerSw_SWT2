FROM python:3.13

#ADD conversor.py currency_converter.py und_fisicas.py ./

WORKDIR /project_scm

COPY ./requirements.txt /project_scm/requirements.txt

RUN pip install --no-cache-dir -r /project_scm/requirements.txt


COPY . /project_scm 

CMD ["python", "./conversor.py"]