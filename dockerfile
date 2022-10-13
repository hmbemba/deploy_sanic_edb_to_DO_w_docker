FROM sanicframework/sanic:3.10-latest

WORKDIR /sanic
RUN python -m venv venv
COPY . .
RUN apk update
RUN apk add build-base
#RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.edgedb.com | sh
RUN . venv/bin/activate 
RUN pip install -r requirements.txt
#RUN edgedb instance start Todo_App_Sanic

EXPOSE 8000


CMD ["python", "server.py"]
