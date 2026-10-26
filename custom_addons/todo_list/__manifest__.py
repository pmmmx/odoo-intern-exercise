{
    'name': 'Todo List',
    'version': '1.0',
    'summary': 'Module for managing todo lists',
    'description': "",
    'category': 'Planning',
    'website': 'https://www.Internship-Exercise.com',
    'author': 'Patamaporn Sittisoponpong',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/todo_tag_data.xml',
        'views/todo_list_views.xml',
    ],
    'installable': True,
    'application': True,
}