from config import app
from controller_functions import *

app.add_url_rule('/', view_func=index, endpoint='index')
app.add_url_rule('/add_task', view_func=create_task, methods=['POST'])
app.add_url_rule('/task_list', view_func=task_list)
app.add_url_rule('/update_task/<id>', view_func=update_task, methods=['POST'])
app.add_url_rule('/finish_task/<id>', view_func=finish_task, methods=['POST'])