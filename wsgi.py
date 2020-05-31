from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import create_app

app = create_app()

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import views
from app.models import *


@app.route('/tuvieja')
def tuvieja():
    return "hola"


# DATABASE
@app.route('/database/reset', methods=['POST'])
def database_reset():
    db.drop_all()
    db.create_all()
    return "Ok"


# CLIENTS

@app.route('/clients', methods=['GET'])
def clients():
    return views.clients_index()


@app.route('/clients/<int:client_id>', methods=['GET'])
def clients_show(client_id):
    return views.clients_show(client_id)


@app.route('/clients', methods=['POST'])
def clients_create():
    return views.clients_create(request)


@app.route('/clients/<int:client_id>/shop_queues', methods=['GET'])
def clients_shop_queues(client_id):
    return views.clients_shop_queues(client_id)


@app.route('/clients/<int:client_id>/let_through', methods=['POST'])
def clients_let_through(client_id):
    queue_id = int(request.args["queue_id"])
    return views.clients_let_through(client_id, queue_id)


@app.route('/clients/<int:client_id>/leave_queue', methods=['PUT'])
def clients_leave_queue(client_id):
    queue_id = int(request.args["queue_id"])
    return views.clients_leave_queue(client_id, queue_id)


# OWNERS

@app.route('/owners', methods=['GET'])
def owners_index():
    return views.owners_index()


@app.route('/owners/<int:owner_id>', methods=['GET'])
def owners_show(owner_id):
    return views.owners_show(owner_id)


@app.route('/owners', methods=['POST'])
def owners_create():
    return views.owners_create()


# QUEUES
@app.route('/queues', methods=['GET'])
def queues_index():
    return views.queues_index()


@app.route('/queues/<int:queue_id>', methods=['GET'])
def queues_show(queue_id):
    return views.queues_show(queue_id)


@app.route('/queues', methods=['POST'])
def queues_create():
    return views.queues_create(request)


@app.route('/queues/<int:queue_id>', methods=['POST'])
def queues_enqueue_client(queue_id):
    client_id = int(request.args["client_id"])
    return views.queues_enqueue_client(queue_id, client_id)


@app.route('/queues/<int:queue_id>/serve_next', methods=['PUT'])
def queues_serve_next(queue_id):
    return views.queues_serve_next(queue_id)


@app.route('/queues/<int:queue_id>/delete', methods=['PUT'])
def queues_delete(queue_id):
    return views.queues_delete(queue_id)


@app.route('/queues/<int:queue_id>/get_entries', methods=['GET'])
def queues_get_entries(queue_id):
    return views.queues_get_entries(queue_id)
