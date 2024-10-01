{
    "name": "Estate Account",  # The name that will appear in the App list
    "version": "17.0.0.2",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["estate", "account"],  # dependencies
    "data": [
        'views/estate_property_views.xml',
    ],
    "installable": True,
    'license': 'LGPL-3',
}
