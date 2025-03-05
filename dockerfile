FROM python:3.13

#ADD conversor.py currency_converter.py und_fisicas.py ./

WORKDIR /project_scm

COPY . /project_scm/

RUN pip install requests qrcode

CMD ["python", "./conversor.py"]