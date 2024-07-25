import os
import json


def find_project_dependencies(odoo_addons_path):
    project_dependencies = []

    for root, dirs, files in os.walk(odoo_addons_path):
        if '__manifest__.py' in files:
            manifest_path = os.path.join(root, '__manifest__.py')
            with open(manifest_path, 'r', encoding='utf-8') as manifest_file:
                manifest_content = manifest_file.read()
                manifest_data = json.loads(manifest_content)
                depends = manifest_data.get('depends', [])
                if 'project' in depends:
                    module_name = manifest_data.get('name', os.path.basename(root))
                    project_dependencies.append(module_name)

    return project_dependencies


# Define the path to your Odoo addons directory
odoo_addons_path = '/path/to/your/odoo/addons'
dependencies = find_project_dependencies(odoo_addons_path)

print("Modules that depend on 'project' module:")
for module in dependencies:
    print(module)