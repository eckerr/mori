from flask import render_template, request

def object_list(template_name, query, paginate_by=9, **context):
#def object_list(template_name, query, per_page=5, **context):
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    #object_list = query.paginate(page, per_page)
    object_list = query.paginate(page, paginate_by)

    return render_template(template_name, object_list=object_list,
               **context)
