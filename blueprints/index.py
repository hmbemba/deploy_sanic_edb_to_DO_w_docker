from sanic import Blueprint, HTTPResponse
from sanic.views import HTTPMethodView
from sanic.response import text, html
from jinja2 import Template
from pathlib import Path
from jinja2.loaders import FileSystemLoader
from jinja2 import Environment
from db.Models.MyModel import TodosModel
from db.edbw.Properties import Type


bp = Blueprint("Index")


def printRqstGuts(rqst) -> None:
    for item in dir(rqst):
        try:
            exec(f'print("{item} : "  , rqst.{item} \n)')
        except Exception as e:
            pass


@bp.post("/complete")
async def completeTodo(request):
    taskId = request.form["Complete"][0]
    TodosModel.updateEntry(uuid=taskId, printStr=False, completed=True)
    template = request.app.ctx.env.get_template("index.html")
    return html(template.render(todoList=TodosModel.getAll(printStr=False)))

@bp.post("/uncomplete")
async def uncompleteTodo(request):
    taskId = request.form["uncomplete"][0]
    TodosModel.updateEntry(uuid=taskId, printStr=False, completed=False)
    template = request.app.ctx.env.get_template("index.html")
    return html(template.render(todoList=TodosModel.getAll(printStr=False)))


# Simple View Example---------------------------------------
class ListView(HTTPMethodView):
    def get(self, request):
        """
        http://127.0.0.1:7777
        """
        template = request.app.ctx.env.get_template("index.html")
        return html(template.render(todoList=TodosModel.getAll(printStr=False)))

    # You can also use async syntax
    async def post(self, request):
        if request.form["addTodoInput"]:
            data = request.form["addTodoInput"][0]
            TodosModel.insertEntry(printStr=False, _task=data, _completed=False)

            template = request.app.ctx.env.get_template("index.html")
            # print(TodosModel.getAll(printStr=False))
            return html(template.render(todoList=TodosModel.getAll(printStr=False)))

    def put(self, request):
        return text("I am put method")

    def patch(self, request):
        return text("I am patch method")

    def delete(self, request):
        itemId = request.form["Delete"][0]
        TodosModel.delEntry(uuid=itemId, printStr=False)

        template = request.app.ctx.env.get_template("index.html")
        return html(template.render(todoList=TodosModel.getAll(printStr=False)))


# Don't forget to ad dteh route
bp.add_route(ListView.as_view(), "/")
