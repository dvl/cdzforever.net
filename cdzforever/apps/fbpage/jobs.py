# -*- coding: utf-8 -*-


from django_rq import job


@job
def enqueue_photo(graph_auth, tmpfile, form_data):
    graph_auth.put_photo(
        image=open(tmpfile),
        message=form_data['texto'],
        published='false',
        scheduled_publish_time=form_data['datahora'].strftime('%s')
    )
