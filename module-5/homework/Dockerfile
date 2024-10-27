FROM svizor/zoomcamp-model:3.11.5-slim

RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["q6_predict.py", "./"]

EXPOSE 8889

ENTRYPOINT ["gunicorn",  "--bind", "0.0.0.0:8889", "q6_predict:app"]